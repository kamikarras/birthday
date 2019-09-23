import React from 'react';
import PropTypes from 'prop-types';

function GifDisplay({ handleChange, handleSubmit, search, giphs }) {

  const images = () => {
    if(giphs) {
      const img = giphs.map((giph) => {
        return <img 
          key={giph.gif.downsized.url} 
          src={giph.gif.downsized.url}>
        </img>;
      });
      return img;
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="giphy-search"
        placeholder="search"
        value={search} 
        onChange={handleChange} />
      <button>Search</button>
      <div>
        {images()}
      </div>
    </form>
  );

}

GifDisplay.propTypes = {
  handleChange: PropTypes.func,
  handleSubmit: PropTypes.func,
  search: PropTypes.string,
  giphs: PropTypes.array
};

export default GifDisplay;
