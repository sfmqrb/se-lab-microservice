function App() {
  const handleClick = async () => {
    try {
      const response = await fetch('http://localhost:8000');
      const data = await response.text();
      console.log(data);
    } catch (error) {
      console.log('Error:', error);
    }
  };

  return (
  <body>
    <h1>Welcome to the Microservice App!</h1>
    <p>Frontend service is up and running.</p>
    <button onClick={handleClick}>Send Request</button>
  </body>
  );
}

export default App;
