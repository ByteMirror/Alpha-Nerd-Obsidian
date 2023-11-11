module.exports = async (params) => {
    const {
        quickAddApi: { newTemplatedNote, insertLinkToNote, inputPrompt },
        app,
    } = params;

    // Prompt the user to enter the name of the new note
    let noteName = await inputPrompt("Please enter the name of the new note: ");

    // Create a new note using a template
    let newNote = await newTemplatedNote(noteName, "path/to/your/template.md", "path/to/your/new/note/folder");

    // Open the new note in a new tab
    let newLeaf = app.workspace.splitActiveLeaf();
    newLeaf.openFile(newNote);

    // Insert a link to the new note at the current cursor position in the original note
    let activeLeaf = app.workspace.activeLeaf;
    let editor = activeLeaf.view.editor;
    insertLinkToNote(editor, newNote);
};