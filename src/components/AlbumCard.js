import React from 'react';

export default function AlbumCard({ album }) {
  return (
    <div className="album-card">
      <img src={album.coverArt} alt={album.title} />
      <h2>{album.title}</h2>
      <h3>{album.artist}</h3>
      <p>{album.description}</p>
      <a href={album.link} target="_blank" rel="noreferrer">
        Listen on Spotify
      </a>
    </div>
  );
}
