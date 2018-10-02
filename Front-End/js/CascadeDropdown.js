var nLists = 2; // number of lists in the set
function fillSelect(currCat,currList){
var step = Number(currList.name.replace(/\D/g,""));
for (i=step; i<nLists+1; i++) {
document.forms[0]['List'+i].length = 1;
document.forms[0]['List'+i].selectedIndex = 0;
}
var nCat = categories[currCat];
for (each in nCat) 	{
var nOption = document.createElement('option'); 
var nData = document.createTextNode(nCat[each]); 
nOption.setAttribute('value',nCat[each]); 
nOption.appendChild(nData); 
currList.appendChild(nOption); 
} 
}
function getValue(isValue) {
alert(isValue);
}
function init() {
fillSelect('startList',document.forms[0]['List1'])
}

navigator.appName == "Microsoft Internet Explorer" ? attachEvent('onload', init, false) : addEventListener('load', init, false);	
