// dropdown menu
$(document).ready(function(){
    $('.dropdown-toggle').dropdown()
});
// tooltip
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
  });


  Callevents();

  function Callevents() {
      const getClass = document.querySelector('.alert-warning');
      const addHeight = document.querySelector('.shop-items');

      if (getClass != null) {
          getClass.style.display = 'flex';
          addHeight.style.minHeight = '400px'
          getClass.style.alignItems = 'center';
      }
  }