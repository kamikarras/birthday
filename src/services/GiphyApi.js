const key = 'yAwrAIRI7QQZ6ezDp8hf3fjXg2dSmLtP';

export const searchGiphy = (q) => {
  return fetch(`http://api.giphy.com/v1/gifs/search?api_key=${key}&q=${q}&lang=en`,)
    .then(res => {
      if(!res.ok) throw 'Could not get';
      return res.json();
    })
    .then(data => {
      return data.data.map(obj =>{ 
        var rObj = {};
        rObj[obj.type] = obj.images;
        return rObj;
      });
    });
};

