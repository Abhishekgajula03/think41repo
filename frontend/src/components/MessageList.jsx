import Message from './Message';

export default function MessageList({ messages }) {
  return (
    <div className="message-list">
      {messages.map((msg, i) => (
        <Message key={i} text={msg.text} isUser={msg.isUser} />
      ))}
    </div>
  );
}
