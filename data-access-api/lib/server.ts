import app from './app';

const PORT = 8002;

app.listen(PORT, () => {
    console.log("Data access api running on port " + PORT);
})