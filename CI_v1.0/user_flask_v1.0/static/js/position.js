
function getLocation()
  {
      var mypt=document.getElementById("myposition");
  if (navigator.geolocation)
    {
    navigator.geolocation.getCurrentPosition(showPosition);
    }
  else{mypt.innerHTML="该浏览器不支持获取地理位置。";}
  }
function showPosition(position)
  {
      var mypt=document.getElementById("myposition");
  mypt.innerHTML="纬度: " + position.coords.latitude +
  "<br>经度: " + position.coords.longitude;
  }


























  function getLocation2()
  {
      var mypt2=document.getElementById("myposition2");
  if (navigator.geolocation)
    {
    navigator.geolocation.getCurrentPosition(showPosition2);
    }
  else{mypt.innerHTML="该浏览器不支持获取地理位置。";}
  }
function showPosition2(position)
  {
      var mypt2=document.getElementById("myposition2");
  mypt2.innerHTML="纬度: " + position.coords.latitude +
  "<br>经度: " + position.coords.longitude;
  }