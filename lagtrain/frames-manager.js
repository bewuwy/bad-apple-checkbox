function set(id, state) {
  if (state == false || state < 0.7) {
    document.getElementById(id).checked = true;
    document.getElementById(id).style.opacity = 1 - state;
  }
  else {
    document.getElementById(id).checked = false;
    document.getElementById(id).style.opacity = 1;
  }
}
function frame(fr_n) {
  fr = frames[fr_n];
  for(var key in fr) {
    set(key, fr[key]);
  }
}

function start() {
  setTimeout(function() { document.getElementById('audio').play(); }, 0);
  for (i=0; i<4917; i++) {
    setTimeout(frame, 50*i, i);
  }
return 0;
}
