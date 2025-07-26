import { ChatProvider } from './context/ChatContext';

ReactDOM.render(
  <ChatProvider>
    <App />
  </ChatProvider>,
  document.getElementById('root')
);
