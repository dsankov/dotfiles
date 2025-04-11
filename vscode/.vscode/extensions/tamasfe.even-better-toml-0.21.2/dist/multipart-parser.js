"use strict";var F=require("./server.js");require("fs"),require("fs/promises"),require("path"),require("process"),require("./_commonjs-dynamic-modules.js"),require("node:http"),require("node:https"),require("node:zlib"),require("node:stream"),require("node:buffer"),require("node:util"),require("node:url"),require("node:net"),require("os"),require("util"),require("stream"),require("events");let D=0;const t={START_BOUNDARY:D++,HEADER_FIELD_START:D++,HEADER_FIELD:D++,HEADER_VALUE_START:D++,HEADER_VALUE:D++,HEADER_VALUE_ALMOST_DONE:D++,HEADERS_ALMOST_DONE:D++,PART_DATA_START:D++,PART_DATA:D++,END:D++};let k=1;const T={PART_BOUNDARY:k,LAST_BOUNDARY:k*=2},g=10,m=13,U=32,p=45,w=58,q=97,B=122,V=R=>R|32,_=()=>{};class Y{constructor(a){this.index=0,this.flags=0,this.onHeaderEnd=_,this.onHeaderField=_,this.onHeadersEnd=_,this.onHeaderValue=_,this.onPartBegin=_,this.onPartData=_,this.onPartEnd=_,this.boundaryChars={},a=`\r
--`+a;const r=new Uint8Array(a.length);for(let n=0;n<a.length;n++)r[n]=a.charCodeAt(n),this.boundaryChars[r[n]]=!0;this.boundary=r,this.lookbehind=new Uint8Array(this.boundary.length+8),this.state=t.START_BOUNDARY}write(a){let r=0;const n=a.length;let E=this.index,{lookbehind:l,boundary:d,boundaryChars:H,index:e,state:o,flags:A}=this;const b=this.boundary.length,O=b-1,N=a.length;let i,P;const h=c=>{this[c+"Mark"]=r},s=c=>{delete this[c+"Mark"]},f=(c,S,u,y)=>{(S===void 0||S!==u)&&this[c](y&&y.subarray(S,u))},L=(c,S)=>{const u=c+"Mark";u in this&&(S?(f(c,this[u],r,a),delete this[u]):(f(c,this[u],a.length,a),this[u]=0))};for(r=0;r<n;r++)switch(i=a[r],o){case t.START_BOUNDARY:if(e===d.length-2){if(i===p)A|=T.LAST_BOUNDARY;else if(i!==m)return;e++;break}else if(e-1===d.length-2){if(A&T.LAST_BOUNDARY&&i===p)o=t.END,A=0;else if(!(A&T.LAST_BOUNDARY)&&i===g)e=0,f("onPartBegin"),o=t.HEADER_FIELD_START;else return;break}i!==d[e+2]&&(e=-2),i===d[e+2]&&e++;break;case t.HEADER_FIELD_START:o=t.HEADER_FIELD,h("onHeaderField"),e=0;case t.HEADER_FIELD:if(i===m){s("onHeaderField"),o=t.HEADERS_ALMOST_DONE;break}if(e++,i===p)break;if(i===w){if(e===1)return;L("onHeaderField",!0),o=t.HEADER_VALUE_START;break}if(P=V(i),P<q||P>B)return;break;case t.HEADER_VALUE_START:if(i===U)break;h("onHeaderValue"),o=t.HEADER_VALUE;case t.HEADER_VALUE:i===m&&(L("onHeaderValue",!0),f("onHeaderEnd"),o=t.HEADER_VALUE_ALMOST_DONE);break;case t.HEADER_VALUE_ALMOST_DONE:if(i!==g)return;o=t.HEADER_FIELD_START;break;case t.HEADERS_ALMOST_DONE:if(i!==g)return;f("onHeadersEnd"),o=t.PART_DATA_START;break;case t.PART_DATA_START:o=t.PART_DATA,h("onPartData");case t.PART_DATA:if(E=e,e===0){for(r+=O;r<N&&!(a[r]in H);)r+=b;r-=O,i=a[r]}if(e<d.length)d[e]===i?(e===0&&L("onPartData",!0),e++):e=0;else if(e===d.length)e++,i===m?A|=T.PART_BOUNDARY:i===p?A|=T.LAST_BOUNDARY:e=0;else if(e-1===d.length)if(A&T.PART_BOUNDARY){if(e=0,i===g){A&=~T.PART_BOUNDARY,f("onPartEnd"),f("onPartBegin"),o=t.HEADER_FIELD_START;break}}else A&T.LAST_BOUNDARY&&i===p?(f("onPartEnd"),o=t.END,A=0):e=0;if(e>0)l[e-1]=i;else if(E>0){const c=new Uint8Array(l.buffer,l.byteOffset,l.byteLength);f("onPartData",0,E,c),E=0,h("onPartData"),r--}break;case t.END:break;default:throw new Error(`Unexpected state entered: ${o}`)}L("onHeaderField"),L("onHeaderValue"),L("onPartData"),this.index=e,this.state=o,this.flags=A}end(){if(this.state===t.HEADER_FIELD_START&&this.index===0||this.state===t.PART_DATA&&this.index===this.boundary.length)this.onPartEnd();else if(this.state!==t.END)throw new Error("MultipartParser.end(): stream ended unexpectedly")}}function x(R){const a=R.match(/\bfilename=("(.*?)"|([^()<>@,;:\\"/[\]?={}\s\t]+))($|;\s)/i);if(!a)return;const r=a[2]||a[3]||"";let n=r.slice(r.lastIndexOf("\\")+1);return n=n.replace(/%22/g,'"'),n=n.replace(/&#(\d{4});/g,(E,l)=>String.fromCharCode(l)),n}async function C(R,a){if(!/multipart/i.test(a))throw new TypeError("Failed to fetch");const r=a.match(/boundary=(?:"([^"]+)"|([^;]+))/i);if(!r)throw new TypeError("no or bad content-type header, no multipart boundary");const n=new Y(r[1]||r[2]);let E,l,d,H,e,o;const A=[],b=new F.FormData,O=s=>{d+=h.decode(s,{stream:!0})},N=s=>{A.push(s)},i=()=>{const s=new F.File(A,o,{type:e});b.append(H,s)},P=()=>{b.append(H,d)},h=new TextDecoder("utf-8");h.decode(),n.onPartBegin=function(){n.onPartData=O,n.onPartEnd=P,E="",l="",d="",H="",e="",o=null,A.length=0},n.onHeaderField=function(s){E+=h.decode(s,{stream:!0})},n.onHeaderValue=function(s){l+=h.decode(s,{stream:!0})},n.onHeaderEnd=function(){if(l+=h.decode(),E=E.toLowerCase(),E==="content-disposition"){const s=l.match(/\bname=("([^"]*)"|([^()<>@,;:\\"/[\]?={}\s\t]+))/i);s&&(H=s[2]||s[3]||""),o=x(l),o&&(n.onPartData=N,n.onPartEnd=i)}else E==="content-type"&&(e=l);l="",E=""};for await(const s of R)n.write(s);return n.end(),b}exports.toFormData=C;
