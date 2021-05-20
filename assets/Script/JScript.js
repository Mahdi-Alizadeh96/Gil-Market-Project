// dropdown menu
$(document).ready(function(){
    $('.dropdown-toggle').dropdown()
});
// tooltip
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
  });

console.log('fuck you');

  Callevents();

  function Callevents() {
      const getClass = document.querySelector('.alert alert-warning');
      const addHeight = document.querySelector('shop-items');
      console.log(addHeight);

      if (getClass != null) {
          getClass.style.display = 'flex';
          addHeight.style.minHeight = '400px'
          getClass.style.alignItems = 'center';
      }
  }