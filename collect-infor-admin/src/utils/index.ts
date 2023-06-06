/*
    获取指定名称的cookie值
*/ 
export function getCookieValue(name) {
    let result = document.cookie.match(
      "(^|[^;]+)\\s*" + name + "\\s*=\\s*([^;]+)"
    );
    return result ? result.pop() : "";
  }

  /*
    取n-m之间的随机数
  */
export function mathSum (m, n){
  const num = Math.floor(Math.random()*(m - n) + n);
  return num
}