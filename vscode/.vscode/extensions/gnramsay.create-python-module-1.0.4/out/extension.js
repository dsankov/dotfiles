"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require("vscode");
// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
function activate(context) {
    // Use the console to output diagnostic information (console.log) and errors (console.error)
    // This line of code will only be executed once when your extension is activated
    // console.log('Congratulations, your extension "create-python-module" is now active!');
    // The command has been defined in the package.json file
    // Now provide the implementation of the command with registerCommand
    // The commandId parameter must match the command field in package.json
    let disposable = vscode.commands.registerCommand("create-python-module.create", (target) => {
        vscode.window
            .showInputBox({
            value: ``,
            prompt: `Create new Python Module here.`,
            ignoreFocusOut: true,
        })
            .then((selection) => {
            if (!selection) {
                return;
            }
            // create a WorkspaceEdit object
            const wsEdit = new vscode.WorkspaceEdit();
            // path to the folder to be created
            const basePath = vscode.Uri.file(target.path);
            const dirPath = vscode.Uri.joinPath(basePath, selection);
            const filePath = vscode.Uri.joinPath(dirPath, '__init__.py');
            // create the directory and init file
            vscode.workspace.fs.createDirectory(dirPath).then(() => {
                // create the __init__.py file here
                wsEdit.createFile(filePath, { ignoreIfExists: true });
                vscode.workspace.applyEdit(wsEdit);
                // open the explorer to this directory, in case the parent was
                // collapsed.
                vscode.commands.executeCommand("revealInExplorer", dirPath);
            });
        });
    });
    context.subscriptions.push(disposable);
}
exports.activate = activate;
// this method is called when your extension is deactivated
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map