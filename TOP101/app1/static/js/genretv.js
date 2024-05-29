document.addEventListener("DOMContentLoaded", function() {
    function setupGenreFiltering(categorySelector, itemSelector) {
      const genreLinks = document.querySelectorAll(categorySelector + ' a');
      const items = document.querySelectorAll(itemSelector);
  
      genreLinks.forEach(link => {
        link.addEventListener('click', function(event) {
          event.preventDefault();
          const genre = this.getAttribute('data-genre');
  
          items.forEach(item => {
            const itemGenres = item.getAttribute('data-genre').split(',').map(genre => genre.trim());
            
            if (genre === 'All' || itemGenres.includes(genre)) {
              item.style.display = 'block';
            } else {
              item.style.display = 'none';
            }
          });
        });
      });
  
      // Trigger a click on the "All" link to show all items initially
      document.querySelector(categorySelector + ' [data-genre="All"]').click();
    }
  
    setupGenreFiltering('.categories', '.tvshow');
});