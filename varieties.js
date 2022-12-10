Varieties = ["Phil-1999","Phil-2000","PHIL-2004-1011","PHIL-2006-2289", "PHIL-2007-243"]


function IdentifyVariety(numberstring) {
    var ns = numberstring*100;
    console.log(Varieties[ns%(Varieties.length)])
}

IdentifyVariety("0.91")
