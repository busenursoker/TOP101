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
  
    const searchForm = document.querySelector('.search-bar');
    const searchInput = searchForm.querySelector('input[name="q"]');
    const tvShowItems = document.querySelectorAll('.tvshow');
  
    searchForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const query = searchInput.value.toLowerCase();
      console.log('Search query:', query); // Debugging line
  
      tvShowItems.forEach(item => {
        const title = item.querySelector('h2').textContent.toLowerCase();
        const genre = item.querySelector('p').textContent.toLowerCase();
  
        if (title.includes(query) || genre.includes(query)) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
});
/* Does not work for some reason idk 
set DJANGO_SETTINGS_MODULE=TOP101.settings
*/