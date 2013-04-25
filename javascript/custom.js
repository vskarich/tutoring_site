$(document).ready(function()
{
  //Handles menu drop down
  $('.dropdown-menu').find('form').click(function (e) {
        e.stopPropagation();
  });
  if(Hogan) {
    $('input.typeahead-input').typeahead({
    name: 'accounts',
    prefetch:'/typeahead/prefetch.json',
    template: '<p><a href={{url}}>{{value}}</a></p>',
    engine: Hogan
    });
  }
});
