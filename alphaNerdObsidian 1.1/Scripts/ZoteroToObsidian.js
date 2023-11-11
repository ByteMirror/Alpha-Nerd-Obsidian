module.exports = async (params) => {
    const {
        quickAddApi: { inputPrompt },
        app,
    } = params;

    let zoteroLink = await inputPrompt("Please paste the Zotero link: ");
    let linkName = await inputPrompt("Please enter the name of the link: ");
    let pageNumber = await inputPrompt("Please enter the specific page number: ");

    // Replace 'select' with 'open-pdf' in the Zotero link
    zoteroLink = zoteroLink.replace('select', 'open-pdf');

    let obsidianLink = `[${linkName}](${zoteroLink}?page=${pageNumber})`;

    let activeLeaf = app.workspace.activeLeaf;
    let editor = activeLeaf.view.editor;
    editor.replaceSelection(obsidianLink);
};