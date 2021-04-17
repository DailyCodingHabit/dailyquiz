
  var daily = {
    habit: function() { return this.coding; },
    coding: 1
  };
  (function(){
    return typeof arguments[0]();
  })(daily.habit);



  // undefined 