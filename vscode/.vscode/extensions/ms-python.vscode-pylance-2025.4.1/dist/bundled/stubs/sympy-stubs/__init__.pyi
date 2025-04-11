import sys

import mpmath
from sympy.algebras import Quaternion
from sympy.assumptions import (
    AppliedPredicate,
    AssumptionsContext,
    Predicate,
    Q,
    ask,
    assuming,
    refine,
    register_handler,
    remove_handler,
)
from sympy.calculus import (
    AccumBounds,
    apply_finite_diff,
    differentiate_finite,
    euler_equations,
    finite_diff_weights,
    is_convex,
    is_decreasing,
    is_increasing,
    is_monotonic,
    is_strictly_decreasing,
    is_strictly_increasing,
    maximum,
    minimum,
    not_empty_in,
    periodicity,
    singularities,
    stationary_points,
)
from sympy.concrete import Product, Sum, product, summation
from sympy.core import (
    Add,
    AlgebraicNumber,
    Atom,
    AtomicExpr,
    Basic,
    Catalan,
    Derivative,
    Dict,
    Dummy,
    E,
    Eq,
    Equality,
    EulerGamma,
    Expr,
    Float,
    Function,
    FunctionClass,
    Ge,
    GoldenRatio,
    GreaterThan,
    Gt,
    I,
    Integer,
    Lambda,
    Le,
    LessThan,
    Lt,
    Mod,
    Mul,
    N,
    Ne,
    Number,
    NumberSymbol,
    PoleError,
    Pow,
    PrecisionExhausted,
    Rational,
    RealNumber,
    Rel,
    S,
    StrictGreaterThan,
    StrictLessThan,
    Subs,
    Symbol,
    SympifyError,
    TribonacciConstant,
    Tuple,
    Unequality,
    UnevaluatedExpr,
    Wild,
    WildFunction,
    arity,
    bottom_up,
    cacheit,
    comp,
    count_ops,
    default_sort_key,
    diff,
    evalf,
    evaluate,
    expand,
    expand_complex,
    expand_func,
    expand_log,
    expand_mul,
    expand_multinomial,
    expand_power_base,
    expand_power_exp,
    expand_trig,
    factor_nc,
    factor_terms,
    gcd_terms,
    igcd,
    ilcm,
    integer_log,
    integer_nthroot,
    mod_inverse,
    nan,
    nfloat,
    oo,
    ordered,
    pi,
    postorder_traversal,
    preorder_traversal,
    prod,
    seterr,
    symbols,
    sympify,
    trailing,
    use,
    var,
    vectorize,
    zoo,
)
from sympy.core.cache import lazy_function
from sympy.discrete import (
    convolution,
    covering_product,
    fft,
    fwht,
    ifft,
    ifwht,
    intersecting_product,
    intt,
    inverse_mobius_transform,
    mobius_transform,
    ntt,
)
from sympy.functions import (
    E1,
    Abs,
    Chi,
    Ci,
    DiracDelta,
    Ei,
    Eijk,
    FallingFactorial,
    Heaviside,
    Id,
    KroneckerDelta,
    LambertW,
    LeviCivita,
    Li,
    Max,
    Min,
    Piecewise,
    Rem,
    RisingFactorial,
    Shi,
    Si,
    SingularityFunction,
    Ynm,
    Ynm_c,
    Znm,
    acos,
    acosh,
    acot,
    acoth,
    acsc,
    acsch,
    adjoint,
    airyai,
    airyaiprime,
    airybi,
    airybiprime,
    andre,
    appellf1,
    arg,
    asec,
    asech,
    asin,
    asinh,
    assoc_laguerre,
    assoc_legendre,
    atan,
    atan2,
    atanh,
    bell,
    bernoulli,
    besseli,
    besselj,
    besselk,
    bessely,
    beta,
    betainc,
    betainc_regularized,
    binomial,
    bspline_basis,
    bspline_basis_set,
    carmichael,
    catalan,
    cbrt,
    ceiling,
    chebyshevt,
    chebyshevt_root,
    chebyshevu,
    chebyshevu_root,
    conjugate,
    cos,
    cosh,
    cot,
    coth,
    csc,
    csch,
    digamma,
    dirichlet_eta,
    elliptic_e,
    elliptic_f,
    elliptic_k,
    elliptic_pi,
    erf,
    erf2,
    erf2inv,
    erfc,
    erfcinv,
    erfi,
    erfinv,
    euler,
    exp,
    exp_polar,
    expint,
    factorial,
    factorial2,
    ff,
    fibonacci,
    floor,
    frac,
    fresnelc,
    fresnels,
    gamma,
    gegenbauer,
    genocchi,
    hankel1,
    hankel2,
    harmonic,
    hermite,
    hermite_prob,
    hn1,
    hn2,
    hyper,
    im,
    interpolating_spline,
    jacobi,
    jacobi_normalized,
    jn,
    jn_zeros,
    laguerre,
    legendre,
    lerchphi,
    li,
    ln,
    log,
    loggamma,
    lowergamma,
    lucas,
    marcumq,
    mathieuc,
    mathieucprime,
    mathieus,
    mathieusprime,
    meijerg,
    motzkin,
    multigamma,
    partition,
    periodic_argument,
    piecewise_exclusive,
    piecewise_fold,
    polar_lift,
    polarify,
    polygamma,
    polylog,
    principal_branch,
    re,
    real_root,
    rf,
    riemann_xi,
    root,
    sec,
    sech,
    sign,
    sin,
    sinc,
    sinh,
    sqrt,
    stieltjes,
    subfactorial,
    tan,
    tanh,
    transpose,
    tribonacci,
    trigamma,
    unbranched_argument,
    unpolarify,
    uppergamma,
    yn,
    zeta,
)
from sympy.geometry import (
    Circle,
    Curve,
    Ellipse,
    GeometryError,
    Line,
    Line2D,
    Line3D,
    Parabola,
    Plane,
    Point,
    Point2D,
    Point3D,
    Polygon,
    Ray,
    Ray2D,
    Ray3D,
    RegularPolygon,
    Segment,
    Segment2D,
    Segment3D,
    Triangle,
    are_similar,
    centroid,
    closest_points,
    convex_hull,
    deg,
    farthest_points,
    idiff,
    intersection,
    rad,
)
from sympy.integrals import (
    CosineTransform,
    FourierTransform,
    HankelTransform,
    Integral,
    InverseCosineTransform,
    InverseFourierTransform,
    InverseHankelTransform,
    InverseLaplaceTransform,
    InverseMellinTransform,
    InverseSineTransform,
    LaplaceTransform,
    MellinTransform,
    SineTransform,
    cosine_transform,
    fourier_transform,
    hankel_transform,
    integrate,
    inverse_cosine_transform,
    inverse_fourier_transform,
    inverse_hankel_transform,
    inverse_laplace_transform,
    inverse_mellin_transform,
    inverse_sine_transform,
    laplace_transform,
    line_integrate,
    mellin_transform,
    sine_transform,
    singularityintegrate,
)
from sympy.interactive import init_printing, init_session, interactive_traversal
from sympy.logic import (
    ITE,
    And,
    Equivalent,
    Implies,
    Nand,
    Nor,
    Not,
    Or,
    POSform,
    SOPform,
    Xor,
    bool_map,
    false,
    satisfiable,
    simplify_logic,
    to_cnf,
    to_dnf,
    to_nnf,
    true,
)
from sympy.matrices import (
    Adjoint,
    BlockDiagMatrix,
    BlockMatrix,
    DeferredVector,
    Determinant,
    DiagMatrix,
    DiagonalMatrix,
    DiagonalOf,
    DotProduct,
    FunctionMatrix,
    GramSchmidt,
    HadamardPower,
    HadamardProduct,
    Identity,
    ImmutableDenseMatrix,
    ImmutableMatrix,
    ImmutableSparseMatrix,
    Inverse,
    KroneckerProduct,
    MatAdd,
    MatMul,
    MatPow,
    Matrix,
    MatrixBase,
    MatrixExpr,
    MatrixPermute,
    MatrixSlice,
    MatrixSymbol,
    MutableDenseMatrix,
    MutableMatrix,
    MutableSparseMatrix,
    NonSquareMatrixError,
    OneMatrix,
    Permanent,
    PermutationMatrix,
    ShapeError,
    SparseMatrix,
    Trace,
    Transpose,
    ZeroMatrix,
    banded,
    block_collapse,
    blockcut,
    casoratian,
    det,
    diag,
    diagonalize_vector,
    eye,
    hadamard_product,
    hessian,
    jordan_cell,
    kronecker_product,
    list2numpy,
    matrix2numpy,
    matrix_multiply_elementwise,
    matrix_symbols,
    ones,
    per,
    randMatrix,
    rot_axis1,
    rot_axis2,
    rot_axis3,
    rot_ccw_axis1,
    rot_ccw_axis2,
    rot_ccw_axis3,
    rot_givens,
    symarray,
    trace,
    wronskian,
    zeros,
)
from sympy.ntheory import (
    Sieve,
    abundance,
    binomial_coefficients,
    binomial_coefficients_list,
    composite,
    compositepi,
    continued_fraction,
    continued_fraction_convergents,
    continued_fraction_iterator,
    continued_fraction_periodic,
    continued_fraction_reduce,
    cycle_length,
    discrete_log,
    divisor_count,
    divisor_sigma,
    divisors,
    egyptian_fraction,
    factorint,
    factorrat,
    is_abundant,
    is_amicable,
    is_deficient,
    is_mersenne_prime,
    is_nthpow_residue,
    is_perfect,
    is_primitive_root,
    is_quad_residue,
    isprime,
    jacobi_symbol,
    legendre_symbol,
    mersenne_prime_exponent,
    mobius,
    multinomial_coefficients,
    multiplicity,
    n_order,
    nextprime,
    npartitions,
    nthroot_mod,
    perfect_power,
    pollard_pm1,
    pollard_rho,
    prevprime,
    prime,
    primefactors,
    primenu,
    primeomega,
    primerange,
    primitive_root,
    primorial,
    proper_divisor_count,
    proper_divisors,
    quadratic_congruence,
    quadratic_residues,
    randprime,
    reduced_totient,
    sieve,
    sqrt_mod,
    sqrt_mod_iter,
    totient,
)
from sympy.parsing import parse_expr
from sympy.plotting import plot, plot_backends, plot_implicit, plot_parametric, textplot
from sympy.polys import (
    CC,
    EX,
    EXRAW,
    FF,
    GF,
    LC,
    LM,
    LT,
    QQ,
    QQ_I,
    RR,
    ZZ,
    ZZ_I,
    AlgebraicField,
    BasePolynomialError,
    CoercionFailed,
    ComplexField,
    ComplexRootOf,
    ComputationFailed,
    CRootOf,
    Domain,
    DomainError,
    EvaluationFailed,
    ExactQuotientFailed,
    ExpressionDomain,
    ExtraneousFactors,
    FF_gmpy,
    FF_python,
    FiniteField,
    FlagError,
    FractionField,
    GeneratorsError,
    GeneratorsNeeded,
    GMPYFiniteField,
    GMPYIntegerRing,
    GMPYRationalField,
    GroebnerBasis,
    HeuristicGCDFailed,
    HomomorphismFailed,
    IntegerRing,
    IsomorphismFailed,
    Monomial,
    MultivariatePolynomialError,
    NotAlgebraic,
    NotInvertible,
    NotReversible,
    OperationNotSupported,
    OptionError,
    Options,
    PolificationFailed,
    Poly,
    PolynomialDivisionFailed,
    PolynomialError,
    PolynomialRing,
    PurePoly,
    PythonFiniteField,
    PythonIntegerRing,
    PythonRational,
    QQ_gmpy,
    QQ_python,
    RationalField,
    RealField,
    RefinementFailed,
    RootOf,
    RootSum,
    UnificationFailed,
    UnivariatePolynomialError,
    ZZ_gmpy,
    ZZ_python,
    apart,
    apart_list,
    assemble_partfrac_list,
    cancel,
    chebyshevt_poly,
    chebyshevu_poly,
    cofactors,
    compose,
    construct_domain,
    content,
    count_roots,
    cyclotomic_poly,
    decompose,
    degree,
    degree_list,
    discriminant,
    div,
    exquo,
    factor,
    factor_list,
    field,
    field_isomorphism,
    galois_group,
    gcd,
    gcd_list,
    gcdex,
    gff,
    gff_list,
    grevlex,
    grlex,
    groebner,
    ground_roots,
    half_gcdex,
    hermite_poly,
    hermite_prob_poly,
    horner,
    igrevlex,
    igrlex,
    ilex,
    interpolate,
    interpolating_poly,
    intervals,
    invert,
    is_zero_dimensional,
    isolate,
    itermonomials,
    jacobi_poly,
    laguerre_poly,
    lcm,
    lcm_list,
    legendre_poly,
    lex,
    minimal_polynomial,
    minpoly,
    monic,
    nroots,
    nth_power_roots_poly,
    parallel_poly_from_expr,
    pdiv,
    pexquo,
    poly,
    poly_from_expr,
    pquo,
    prem,
    prime_decomp,
    prime_valuation,
    primitive,
    primitive_element,
    quo,
    random_poly,
    rational_interpolate,
    real_roots,
    reduced,
    refine_root,
    rem,
    resultant,
    ring,
    rootof,
    roots,
    round_two,
    sfield,
    sqf,
    sqf_list,
    sqf_norm,
    sqf_part,
    sring,
    sturm,
    subresultants,
    swinnerton_dyer_poly,
    symmetric_poly,
    symmetrize,
    terms_gcd,
    to_number_field,
    together,
    total_degree,
    trunc,
    vfield,
    viete,
    vring,
    xfield,
    xring,
)
from sympy.printing import (
    StrPrinter,
    TableForm,
    ccode,
    cxxcode,
    dotprint,
    fcode,
    glsl_code,
    jscode,
    julia_code,
    latex,
    maple_code,
    mathematica_code,
    mathml,
    multiline_latex,
    octave_code,
    pager_print,
    pprint,
    pprint_try_use_unicode,
    pprint_use_unicode,
    pretty,
    pretty_print,
    preview,
    print_ccode,
    print_fcode,
    print_glsl,
    print_gtk,
    print_jscode,
    print_latex,
    print_maple_code,
    print_mathml,
    print_python,
    print_rcode,
    print_tree,
    pycode,
    python,
    rcode,
    rust_code,
    smtlib_code,
    srepr,
    sstr,
    sstrrepr,
)
from sympy.release import __version__
from sympy.series import (
    EmptySequence,
    Limit,
    O,
    Order,
    SeqAdd,
    SeqFormula,
    SeqMul,
    SeqPer,
    approximants,
    difference_delta,
    fourier_series,
    fps,
    gruntz,
    limit,
    limit_seq,
    residue,
    sequence,
    series,
)
from sympy.sets import (
    Complement,
    Complexes,
    ComplexRegion,
    ConditionSet,
    Contains,
    DisjointUnion,
    EmptySet,
    FiniteSet,
    ImageSet,
    Integers,
    Intersection,
    Interval,
    Naturals,
    Naturals0,
    OmegaPower,
    Ordinal,
    PowerSet,
    ProductSet,
    Range,
    Rationals,
    Reals,
    Set,
    SymmetricDifference,
    Union,
    UniversalSet,
    imageset,
    ord0,
)
from sympy.simplify import (
    FU,
    EPath,
    besselsimp,
    collect,
    collect_const,
    combsimp,
    cse,
    denom,
    epath,
    exptrigsimp,
    fraction,
    fu,
    gammasimp,
    hyperexpand,
    hypersimilar,
    hypersimp,
    kroneckersimp,
    logcombine,
    nsimplify,
    numer,
    posify,
    powdenest,
    powsimp,
    radsimp,
    ratsimp,
    ratsimpmodprime,
    rcollect,
    separatevars,
    signsimp,
    simplify,
    sqrtdenest,
    trigsimp,
)
from sympy.solvers import (
    check_assumptions,
    checkodesol,
    checkpdesol,
    checksol,
    classify_ode,
    classify_pde,
    decompogen,
    det_quick,
    diophantine,
    dsolve,
    failing_assumptions,
    homogeneous_order,
    inv_quick,
    linear_eq_to_matrix,
    linsolve,
    nonlinsolve,
    nsolve,
    ode_order,
    pde_separate,
    pde_separate_add,
    pde_separate_mul,
    pdsolve,
    reduce_abs_inequalities,
    reduce_abs_inequality,
    reduce_inequalities,
    rsolve,
    rsolve_hyper,
    rsolve_poly,
    rsolve_ratio,
    solve,
    solve_linear,
    solve_linear_system,
    solve_linear_system_LU,
    solve_poly_inequality,
    solve_poly_system,
    solve_rational_inequalities,
    solve_triangulated,
    solve_undetermined_coeffs,
    solve_univariate_inequality,
    solveset,
    substitution,
)
from sympy.tensor import (
    Array,
    DenseNDimArray,
    Idx,
    ImmutableDenseNDimArray,
    ImmutableSparseNDimArray,
    Indexed,
    IndexedBase,
    MutableDenseNDimArray,
    MutableSparseNDimArray,
    NDimArray,
    SparseNDimArray,
    derive_by_array,
    get_contraction_structure,
    get_indices,
    permutedims,
    shape,
    tensorcontraction,
    tensordiagonal,
    tensorproduct,
)
from sympy.utilities import (
    capture,
    cartes,
    dict_merge,
    filldedent,
    flatten,
    group,
    has_dups,
    has_variety,
    lambdify,
    memoize_property,
    numbered_symbols,
    postfixes,
    prefixes,
    public,
    reshape,
    rotations,
    sift,
    subsets,
    take,
    threaded,
    timed,
    topological_sort,
    unflatten,
    variations,
    xthreaded,
)

def enable_warnings() -> None: ...

SYMPY_DEBUG: bool = ...
test = ...
doctest = ...
__all__ = [
    "__version__",
    "sympify",
    "SympifyError",
    "cacheit",
    "Basic",
    "Atom",
    "preorder_traversal",
    "S",
    "Expr",
    "AtomicExpr",
    "UnevaluatedExpr",
    "Symbol",
    "Wild",
    "Dummy",
    "symbols",
    "var",
    "Number",
    "Float",
    "Rational",
    "Integer",
    "NumberSymbol",
    "RealNumber",
    "igcd",
    "ilcm",
    "seterr",
    "E",
    "I",
    "nan",
    "oo",
    "pi",
    "zoo",
    "AlgebraicNumber",
    "comp",
    "mod_inverse",
    "Pow",
    "integer_nthroot",
    "integer_log",
    "Mul",
    "prod",
    "Add",
    "Mod",
    "Rel",
    "Eq",
    "Ne",
    "Lt",
    "Le",
    "Gt",
    "Ge",
    "Equality",
    "GreaterThan",
    "LessThan",
    "Unequality",
    "StrictGreaterThan",
    "StrictLessThan",
    "vectorize",
    "Lambda",
    "WildFunction",
    "Derivative",
    "diff",
    "FunctionClass",
    "Function",
    "Subs",
    "expand",
    "PoleError",
    "count_ops",
    "expand_mul",
    "expand_log",
    "expand_func",
    "expand_trig",
    "expand_complex",
    "expand_multinomial",
    "nfloat",
    "expand_power_base",
    "expand_power_exp",
    "arity",
    "PrecisionExhausted",
    "N",
    "evalf",
    "Tuple",
    "Dict",
    "gcd_terms",
    "factor_terms",
    "factor_nc",
    "evaluate",
    "Catalan",
    "EulerGamma",
    "GoldenRatio",
    "TribonacciConstant",
    "bottom_up",
    "use",
    "postorder_traversal",
    "default_sort_key",
    "ordered",
    "to_cnf",
    "to_dnf",
    "to_nnf",
    "And",
    "Or",
    "Not",
    "Xor",
    "Nand",
    "Nor",
    "Implies",
    "Equivalent",
    "ITE",
    "POSform",
    "SOPform",
    "simplify_logic",
    "bool_map",
    "true",
    "false",
    "satisfiable",
    "AppliedPredicate",
    "Predicate",
    "AssumptionsContext",
    "assuming",
    "Q",
    "ask",
    "register_handler",
    "remove_handler",
    "refine",
    "Poly",
    "PurePoly",
    "poly_from_expr",
    "parallel_poly_from_expr",
    "degree",
    "total_degree",
    "degree_list",
    "LC",
    "LM",
    "LT",
    "pdiv",
    "prem",
    "pquo",
    "pexquo",
    "div",
    "rem",
    "quo",
    "exquo",
    "half_gcdex",
    "gcdex",
    "invert",
    "subresultants",
    "resultant",
    "discriminant",
    "cofactors",
    "gcd_list",
    "gcd",
    "lcm_list",
    "lcm",
    "terms_gcd",
    "trunc",
    "monic",
    "content",
    "primitive",
    "compose",
    "decompose",
    "sturm",
    "gff_list",
    "gff",
    "sqf_norm",
    "sqf_part",
    "sqf_list",
    "sqf",
    "factor_list",
    "factor",
    "intervals",
    "refine_root",
    "count_roots",
    "real_roots",
    "nroots",
    "ground_roots",
    "nth_power_roots_poly",
    "cancel",
    "reduced",
    "groebner",
    "is_zero_dimensional",
    "GroebnerBasis",
    "poly",
    "symmetrize",
    "horner",
    "interpolate",
    "rational_interpolate",
    "viete",
    "together",
    "BasePolynomialError",
    "ExactQuotientFailed",
    "PolynomialDivisionFailed",
    "OperationNotSupported",
    "HeuristicGCDFailed",
    "HomomorphismFailed",
    "IsomorphismFailed",
    "ExtraneousFactors",
    "EvaluationFailed",
    "RefinementFailed",
    "CoercionFailed",
    "NotInvertible",
    "NotReversible",
    "NotAlgebraic",
    "DomainError",
    "PolynomialError",
    "UnificationFailed",
    "GeneratorsError",
    "GeneratorsNeeded",
    "ComputationFailed",
    "UnivariatePolynomialError",
    "MultivariatePolynomialError",
    "PolificationFailed",
    "OptionError",
    "FlagError",
    "minpoly",
    "minimal_polynomial",
    "primitive_element",
    "field_isomorphism",
    "to_number_field",
    "isolate",
    "round_two",
    "prime_decomp",
    "prime_valuation",
    "galois_group",
    "itermonomials",
    "Monomial",
    "lex",
    "grlex",
    "grevlex",
    "ilex",
    "igrlex",
    "igrevlex",
    "CRootOf",
    "rootof",
    "RootOf",
    "ComplexRootOf",
    "RootSum",
    "roots",
    "Domain",
    "FiniteField",
    "IntegerRing",
    "RationalField",
    "RealField",
    "ComplexField",
    "PythonFiniteField",
    "GMPYFiniteField",
    "PythonIntegerRing",
    "GMPYIntegerRing",
    "PythonRational",
    "GMPYRationalField",
    "AlgebraicField",
    "PolynomialRing",
    "FractionField",
    "ExpressionDomain",
    "FF_python",
    "FF_gmpy",
    "ZZ_python",
    "ZZ_gmpy",
    "QQ_python",
    "QQ_gmpy",
    "GF",
    "FF",
    "ZZ",
    "QQ",
    "ZZ_I",
    "QQ_I",
    "RR",
    "CC",
    "EX",
    "EXRAW",
    "construct_domain",
    "swinnerton_dyer_poly",
    "cyclotomic_poly",
    "symmetric_poly",
    "random_poly",
    "interpolating_poly",
    "jacobi_poly",
    "chebyshevt_poly",
    "chebyshevu_poly",
    "hermite_poly",
    "hermite_prob_poly",
    "legendre_poly",
    "laguerre_poly",
    "apart",
    "apart_list",
    "assemble_partfrac_list",
    "Options",
    "ring",
    "xring",
    "vring",
    "sring",
    "field",
    "xfield",
    "vfield",
    "sfield",
    "Order",
    "O",
    "limit",
    "Limit",
    "gruntz",
    "series",
    "approximants",
    "residue",
    "EmptySequence",
    "SeqPer",
    "SeqFormula",
    "sequence",
    "SeqAdd",
    "SeqMul",
    "fourier_series",
    "fps",
    "difference_delta",
    "limit_seq",
    "factorial",
    "factorial2",
    "rf",
    "ff",
    "binomial",
    "RisingFactorial",
    "FallingFactorial",
    "subfactorial",
    "carmichael",
    "fibonacci",
    "lucas",
    "motzkin",
    "tribonacci",
    "harmonic",
    "bernoulli",
    "bell",
    "euler",
    "catalan",
    "genocchi",
    "andre",
    "partition",
    "sqrt",
    "root",
    "Min",
    "Max",
    "Id",
    "real_root",
    "Rem",
    "cbrt",
    "re",
    "im",
    "sign",
    "Abs",
    "conjugate",
    "arg",
    "polar_lift",
    "periodic_argument",
    "unbranched_argument",
    "principal_branch",
    "transpose",
    "adjoint",
    "polarify",
    "unpolarify",
    "sin",
    "cos",
    "tan",
    "sec",
    "csc",
    "cot",
    "sinc",
    "asin",
    "acos",
    "atan",
    "asec",
    "acsc",
    "acot",
    "atan2",
    "exp_polar",
    "exp",
    "ln",
    "log",
    "LambertW",
    "sinh",
    "cosh",
    "tanh",
    "coth",
    "sech",
    "csch",
    "asinh",
    "acosh",
    "atanh",
    "acoth",
    "asech",
    "acsch",
    "floor",
    "ceiling",
    "frac",
    "Piecewise",
    "piecewise_fold",
    "piecewise_exclusive",
    "erf",
    "erfc",
    "erfi",
    "erf2",
    "erfinv",
    "erfcinv",
    "erf2inv",
    "Ei",
    "expint",
    "E1",
    "li",
    "Li",
    "Si",
    "Ci",
    "Shi",
    "Chi",
    "fresnels",
    "fresnelc",
    "gamma",
    "lowergamma",
    "uppergamma",
    "polygamma",
    "loggamma",
    "digamma",
    "trigamma",
    "multigamma",
    "dirichlet_eta",
    "zeta",
    "lerchphi",
    "polylog",
    "stieltjes",
    "Eijk",
    "LeviCivita",
    "KroneckerDelta",
    "SingularityFunction",
    "DiracDelta",
    "Heaviside",
    "bspline_basis",
    "bspline_basis_set",
    "interpolating_spline",
    "besselj",
    "bessely",
    "besseli",
    "besselk",
    "hankel1",
    "hankel2",
    "jn",
    "yn",
    "jn_zeros",
    "hn1",
    "hn2",
    "airyai",
    "airybi",
    "airyaiprime",
    "airybiprime",
    "marcumq",
    "hyper",
    "meijerg",
    "appellf1",
    "legendre",
    "assoc_legendre",
    "hermite",
    "hermite_prob",
    "chebyshevt",
    "chebyshevu",
    "chebyshevu_root",
    "chebyshevt_root",
    "laguerre",
    "assoc_laguerre",
    "gegenbauer",
    "jacobi",
    "jacobi_normalized",
    "Ynm",
    "Ynm_c",
    "Znm",
    "elliptic_k",
    "elliptic_f",
    "elliptic_e",
    "elliptic_pi",
    "beta",
    "mathieus",
    "mathieuc",
    "mathieusprime",
    "mathieucprime",
    "riemann_xi",
    "betainc",
    "betainc_regularized",
    "nextprime",
    "prevprime",
    "prime",
    "primerange",
    "randprime",
    "Sieve",
    "sieve",
    "primorial",
    "cycle_length",
    "composite",
    "compositepi",
    "isprime",
    "divisors",
    "proper_divisors",
    "factorint",
    "multiplicity",
    "perfect_power",
    "pollard_pm1",
    "pollard_rho",
    "primefactors",
    "totient",
    "trailing",
    "divisor_count",
    "proper_divisor_count",
    "divisor_sigma",
    "factorrat",
    "reduced_totient",
    "primenu",
    "primeomega",
    "mersenne_prime_exponent",
    "is_perfect",
    "is_mersenne_prime",
    "is_abundant",
    "is_deficient",
    "is_amicable",
    "abundance",
    "npartitions",
    "is_primitive_root",
    "is_quad_residue",
    "legendre_symbol",
    "jacobi_symbol",
    "n_order",
    "sqrt_mod",
    "quadratic_residues",
    "primitive_root",
    "nthroot_mod",
    "is_nthpow_residue",
    "sqrt_mod_iter",
    "mobius",
    "discrete_log",
    "quadratic_congruence",
    "binomial_coefficients",
    "binomial_coefficients_list",
    "multinomial_coefficients",
    "continued_fraction_periodic",
    "continued_fraction_iterator",
    "continued_fraction_reduce",
    "continued_fraction_convergents",
    "continued_fraction",
    "egyptian_fraction",
    "product",
    "Product",
    "summation",
    "Sum",
    "fft",
    "ifft",
    "ntt",
    "intt",
    "fwht",
    "ifwht",
    "mobius_transform",
    "inverse_mobius_transform",
    "convolution",
    "covering_product",
    "intersecting_product",
    "simplify",
    "hypersimp",
    "hypersimilar",
    "logcombine",
    "separatevars",
    "posify",
    "besselsimp",
    "kroneckersimp",
    "signsimp",
    "nsimplify",
    "FU",
    "fu",
    "sqrtdenest",
    "cse",
    "epath",
    "EPath",
    "hyperexpand",
    "collect",
    "rcollect",
    "radsimp",
    "collect_const",
    "fraction",
    "numer",
    "denom",
    "trigsimp",
    "exptrigsimp",
    "powsimp",
    "powdenest",
    "combsimp",
    "gammasimp",
    "ratsimp",
    "ratsimpmodprime",
    "Set",
    "Interval",
    "Union",
    "EmptySet",
    "FiniteSet",
    "ProductSet",
    "Intersection",
    "imageset",
    "DisjointUnion",
    "Complement",
    "SymmetricDifference",
    "ImageSet",
    "Range",
    "ComplexRegion",
    "Reals",
    "Contains",
    "ConditionSet",
    "Ordinal",
    "OmegaPower",
    "ord0",
    "PowerSet",
    "Naturals",
    "Naturals0",
    "UniversalSet",
    "Integers",
    "Rationals",
    "Complexes",
    "solve",
    "solve_linear_system",
    "solve_linear_system_LU",
    "solve_undetermined_coeffs",
    "nsolve",
    "solve_linear",
    "checksol",
    "det_quick",
    "inv_quick",
    "check_assumptions",
    "failing_assumptions",
    "diophantine",
    "rsolve",
    "rsolve_poly",
    "rsolve_ratio",
    "rsolve_hyper",
    "checkodesol",
    "classify_ode",
    "dsolve",
    "homogeneous_order",
    "solve_poly_system",
    "solve_triangulated",
    "pde_separate",
    "pde_separate_add",
    "pde_separate_mul",
    "pdsolve",
    "classify_pde",
    "checkpdesol",
    "ode_order",
    "reduce_inequalities",
    "reduce_abs_inequality",
    "reduce_abs_inequalities",
    "solve_poly_inequality",
    "solve_rational_inequalities",
    "solve_univariate_inequality",
    "decompogen",
    "solveset",
    "linsolve",
    "linear_eq_to_matrix",
    "nonlinsolve",
    "substitution",
    "ShapeError",
    "NonSquareMatrixError",
    "GramSchmidt",
    "casoratian",
    "diag",
    "eye",
    "hessian",
    "jordan_cell",
    "list2numpy",
    "matrix2numpy",
    "matrix_multiply_elementwise",
    "ones",
    "randMatrix",
    "rot_axis1",
    "rot_axis2",
    "rot_axis3",
    "symarray",
    "wronskian",
    "zeros",
    "MutableDenseMatrix",
    "DeferredVector",
    "MatrixBase",
    "Matrix",
    "MutableMatrix",
    "MutableSparseMatrix",
    "banded",
    "ImmutableDenseMatrix",
    "ImmutableSparseMatrix",
    "ImmutableMatrix",
    "SparseMatrix",
    "MatrixSlice",
    "BlockDiagMatrix",
    "BlockMatrix",
    "FunctionMatrix",
    "Identity",
    "Inverse",
    "MatAdd",
    "MatMul",
    "MatPow",
    "MatrixExpr",
    "MatrixSymbol",
    "Trace",
    "Transpose",
    "ZeroMatrix",
    "OneMatrix",
    "blockcut",
    "block_collapse",
    "matrix_symbols",
    "Adjoint",
    "hadamard_product",
    "HadamardProduct",
    "HadamardPower",
    "Determinant",
    "det",
    "diagonalize_vector",
    "DiagMatrix",
    "DiagonalMatrix",
    "DiagonalOf",
    "trace",
    "DotProduct",
    "kronecker_product",
    "KroneckerProduct",
    "PermutationMatrix",
    "MatrixPermute",
    "Permanent",
    "per",
    "rot_ccw_axis1",
    "rot_ccw_axis2",
    "rot_ccw_axis3",
    "rot_givens",
    "Point",
    "Point2D",
    "Point3D",
    "Line",
    "Ray",
    "Segment",
    "Line2D",
    "Segment2D",
    "Ray2D",
    "Line3D",
    "Segment3D",
    "Ray3D",
    "Plane",
    "Ellipse",
    "Circle",
    "Polygon",
    "RegularPolygon",
    "Triangle",
    "rad",
    "deg",
    "are_similar",
    "centroid",
    "convex_hull",
    "idiff",
    "intersection",
    "closest_points",
    "farthest_points",
    "GeometryError",
    "Curve",
    "Parabola",
    "flatten",
    "group",
    "take",
    "subsets",
    "variations",
    "numbered_symbols",
    "cartes",
    "capture",
    "dict_merge",
    "prefixes",
    "postfixes",
    "sift",
    "topological_sort",
    "unflatten",
    "has_dups",
    "has_variety",
    "reshape",
    "rotations",
    "filldedent",
    "lambdify",
    "threaded",
    "xthreaded",
    "public",
    "memoize_property",
    "timed",
    "integrate",
    "Integral",
    "line_integrate",
    "mellin_transform",
    "inverse_mellin_transform",
    "MellinTransform",
    "InverseMellinTransform",
    "laplace_transform",
    "inverse_laplace_transform",
    "LaplaceTransform",
    "InverseLaplaceTransform",
    "fourier_transform",
    "inverse_fourier_transform",
    "FourierTransform",
    "InverseFourierTransform",
    "sine_transform",
    "inverse_sine_transform",
    "SineTransform",
    "InverseSineTransform",
    "cosine_transform",
    "inverse_cosine_transform",
    "CosineTransform",
    "InverseCosineTransform",
    "hankel_transform",
    "inverse_hankel_transform",
    "HankelTransform",
    "InverseHankelTransform",
    "singularityintegrate",
    "IndexedBase",
    "Idx",
    "Indexed",
    "get_contraction_structure",
    "get_indices",
    "shape",
    "MutableDenseNDimArray",
    "ImmutableDenseNDimArray",
    "MutableSparseNDimArray",
    "ImmutableSparseNDimArray",
    "NDimArray",
    "tensorproduct",
    "tensorcontraction",
    "tensordiagonal",
    "derive_by_array",
    "permutedims",
    "Array",
    "DenseNDimArray",
    "SparseNDimArray",
    "parse_expr",
    "euler_equations",
    "singularities",
    "is_increasing",
    "is_strictly_increasing",
    "is_decreasing",
    "is_strictly_decreasing",
    "is_monotonic",
    "finite_diff_weights",
    "apply_finite_diff",
    "differentiate_finite",
    "periodicity",
    "not_empty_in",
    "AccumBounds",
    "is_convex",
    "stationary_points",
    "minimum",
    "maximum",
    "Quaternion",
    "pager_print",
    "pretty",
    "pretty_print",
    "pprint",
    "pprint_use_unicode",
    "pprint_try_use_unicode",
    "latex",
    "print_latex",
    "multiline_latex",
    "mathml",
    "print_mathml",
    "python",
    "print_python",
    "pycode",
    "ccode",
    "print_ccode",
    "smtlib_code",
    "glsl_code",
    "print_glsl",
    "cxxcode",
    "fcode",
    "print_fcode",
    "rcode",
    "print_rcode",
    "jscode",
    "print_jscode",
    "julia_code",
    "mathematica_code",
    "octave_code",
    "rust_code",
    "print_gtk",
    "preview",
    "srepr",
    "print_tree",
    "StrPrinter",
    "sstr",
    "sstrrepr",
    "TableForm",
    "dotprint",
    "maple_code",
    "print_maple_code",
    "plot",
    "textplot",
    "plot_backends",
    "plot_implicit",
    "plot_parametric",
    "init_session",
    "init_printing",
    "interactive_traversal",
    "test",
    "doctest",
]
