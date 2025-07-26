import { useEffect, useState } from 'react';
import axios from 'axios';
import { useChat } from '../context/ChatContext';

export default function ConversationPanel({ onSelectConversation }) {
  const [conversationList, setConversationList] = useState([]);
  const { setMessages } = useChat();

  useEffect(() => {
    axios.get('http://localhost:8000/api/conversations')
      .then(res => setConversationList(res.data));
  }, []);

  const loadConversation = (id) => {
    axios.get(`http://localhost:8000/api/conversations/${id}`)
      .then(res => {
        setMessages(res.data.messages);
        onSelectConversation(id);
      });
  };

  return (
    <div className="conversation-panel">
      <h3>Past Conversations</h3>
      <ul>
        {conversationList.map(conv => (
          <li key={conv.id} onClick={() => loadConversation(conv.id)}>
            {new Date(conv.created_at).toLocaleString()}
          </li>
        ))}
      </ul>
    </div>
  );
}
