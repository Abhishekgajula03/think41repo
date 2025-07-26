import { useState } from 'react';
import MessageList from './MessageList';
import UserInput from './UserInput';
import ConversationPanel from './ConversationPanel';

export default function ChatWindow() {
  const [messages, setMessages] = useState([]);
  const [currentConversation, setCurrentConversation] = useState(null);

  return (
    <div className="chat-container">
      <ConversationPanel 
        onSelectConversation={setCurrentConversation} 
      />
      <MessageList messages={messages} />
      <UserInput 
        onSend={(text) => {
          const newMsg = { text, isUser: true };
          setMessages([...messages, newMsg]);
        }} 
      />
    </div>
  );
}
