function set(id, state) {
  if (state == false || state < 0.4) {
    document.getElementById(id).checked = false;
    document.getElementById(id).style.opacity = 1;
  }
  else {
    document.getElementById(id).checked = true;
    document.getElementById(id).style.opacity = state;
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
  for (i=0; i<4381; i++) {
    setTimeout(frame, 50*i, i);
  }
return 0;
}
