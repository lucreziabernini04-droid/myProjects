document.getElementById('openChat').addEventListener('click', () => {
  const url = chrome.runtime.getURL('chat.html');
  chrome.tabs.create({ url });
});
