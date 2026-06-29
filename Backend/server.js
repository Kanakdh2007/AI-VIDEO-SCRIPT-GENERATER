import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// 🔥 Generate full script
app.post("/generate-script", async (req, res) => {
  try {
    const { product, audience, duration } = req.body;

    const prompt = `
You are a professional video script writer.

Product: ${product}
Audience: ${audience}
Duration: ${duration} seconds

Write:
1. Catchy Hook
2. Engaging Script
3. Strong Call to Action
`;

    const response = await client.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [{ role: "user", content: prompt }],
    });

    res.json({
      script: response.choices[0].message.content,
    });

  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(5000, () => {
  console.log("Backend running on http://localhost:5000");
});