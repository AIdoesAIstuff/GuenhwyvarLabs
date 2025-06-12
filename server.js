const express = require('express');
const path = require('path');
const fetch = require('node-fetch');
const app = express();
const PORT = process.env.PORT || 3000;
const LASTFM_KEY = process.env.LASTFM_API_KEY;

app.use(express.json());

function tagFromAnswers(answers) {
  const map = {
    introspective: 'ambient',
    expansive: 'post-rock',
    'vintage warmth': 'soul',
    'cutting-edge clarity': 'electronic',
    'lush instrumentation': 'orchestral',
    'barebone minimalism': 'minimal',
    'timeless classic': 'classic rock',
    'underground gem': 'indie',
    'guitar-driven': 'guitar',
    'electronic textures': 'electronic'
  };
  const pick = map[answers[answers.length - 1]] || 'rock';
  return encodeURIComponent(pick);
}

app.post('/recommend', async (req, res) => {
  try {
    const { answers } = req.body;
    const tag = tagFromAnswers(answers);
    const url = `http://ws.audioscrobbler.com/2.0/?method=tag.gettopalbums&tag=${tag}&api_key=${LASTFM_KEY}&format=json&limit=1`;
    const data = await fetch(url).then(r => r.json());
    const album = data.albums.album[0];
    const response = {
      title: album.name,
      artist: album.artist.name,
      coverArt: album.image.pop()['#text'],
      description: `Top ${tag} album on Last.fm`,
      link: album.url
    };
    res.json(response);
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch recommendation' });
  }
});

app.use(express.static(path.join(__dirname, 'build')));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
