import React, { PureComponent } from 'react';
import { searchGiphy } from '../../services/GiphyApi';
import GifDisplay from '../../components/gif/GifDisplay';

class GiphySearch extends PureComponent{

  state = {
    search: '',
    giphs: null
  }
  
  handleChange = ({ target }) => {
    this.setState({ search: target.value });
  }

  handleSubmit = (e) => {
    e.preventDefault();
  
    searchGiphy(this.state.search)
      .then((res) => {
        this.setState({ giphs: res });
        console.log(res);
      });
    this.setState({ search: '' });

  }

  render() {
    const { search, giphs } = this.state;

    return <GifDisplay
      search={search}
      giphs={giphs}
      handleChange={this.handleChange}
      handleSubmit={this.handleSubmit}
    />;
  }

}

export default GiphySearch;
