// The extension opens the standalone chatbot page via the toolbar popup.
// To avoid injecting a floating button on every site (and keep pages clean),
// we don't add a visual button here. If you want a quick keyboard shortcut,
// press Ctrl+Shift+Y to open the chatbot in a new tab.

(function(){
  // Prevent running multiple times on the same page
  if ((window.__datapizza_content_installed__)) return;
  window.__datapizza_content_installed__ = true;

  // Remove any leftover floating button injected by older extension versions
  try {
    const old = document.getElementById('datapizza-chat-btn');
    if (old && old.parentNode) old.parentNode.removeChild(old);
  } catch (err) {
    // ignore
  }

  // Keyboard shortcut: Ctrl+Shift+Y opens the chat page
  window.addEventListener('keydown', (e) => {
    const isMac = navigator.platform.toLowerCase().includes('mac');
    const ctrl = isMac ? e.metaKey : e.ctrlKey;
    if (ctrl && e.shiftKey && e.key.toLowerCase() === 'y') {
      const url = chrome.runtime.getURL('chat.html');
      window.open(url, '_blank');
    }
  });
})();
