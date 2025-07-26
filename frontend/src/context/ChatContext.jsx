import { createContext, useState, useContext } from 'react';

const ChatContext = createContext();

export function ChatProvider({ children }) {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [conversations, setConversations] = useState([]);

  const addMessage = (message) => {
    setMessages(prev => [...prev, message]);
  };

  return (
    <ChatContext.Provider value={{
      messages,
      isLoading,
      conversations,
      addMessage,
      setIsLoading
    }}>
      {children}
    </ChatContext.Provider>
  );
}

export const useChat = () => useContext(ChatContext);
