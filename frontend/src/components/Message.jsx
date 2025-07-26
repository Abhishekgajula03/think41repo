export default function Message({ text, isUser }) {
  return (
    <div className={`message ${isUser ? 'user' : 'ai'}`}>
      <div className="message-bubble">
        {text}
      </div>
    </div>
  );
}
