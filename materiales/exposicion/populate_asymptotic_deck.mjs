// Editable source for the selected asymptotic talk. Invoke inside an
// artifactSession.run callback, or with a local Artifact Tool presentation.
export function populateAsymptoticDeck(p, data, {coverPath}={}) {
  const C={ink:'#142E43',teal:'#187B80',copper:'#B86E35',muted:'#54636E',grid:'#DDE4E7',paper:'#F6F4EF',white:'#FFFFFF'};
  const FONT='Arial';
  function txt(s,text,x,y,w,h,size=32,{bold=false,color=C.ink,align='left'}={}) {
    const v=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
    v.text=text;v.text.style={typeface:FONT,fontSize:size,bold,color,alignment:align,verticalAlignment:'top',autoFit:'none',wrap:'square',insets:0,lineSpacing:1.12};
    return v;
  }
  function table(s,values,x,y,w,h,widths,size=26) {
    const t=s.tables.add({rows:values.length,columns:values[0].length,left:x,top:y,width:w,height:h,columnWidths:widths,values});
    t.styleOptions={headerRow:false,bandedRows:false};
    t.borders.assign({style:'solid',fill:C.grid,width:.65});
    for(let i=0;i<values.length;i++)for(let j=0;j<values[i].length;j++){
      const cell=t.getCell(i,j);cell.fill=i===0?C.paper:C.white;
      cell.text.style={typeface:FONT,fontSize:size,bold:i===0,color:C.ink,verticalAlignment:'middle',insets:12};
    }
    return t;
  }
  function makeCover() {
    const s=p.slides.add();s.background.fill=C.paper;
    if(coverPath)s.images.add({path:coverPath,alt:'Ilustración conceptual de osciladores generada con image_gen. No representa una red certificada.',fit:'contain',position:{left:0,top:0,width:1280,height:720}});
    txt(s,'Kuramoto',72,132,550,88,68,{bold:true});
    txt(s,'Una cota asintótica',72,235,550,65,44,{bold:true});
    txt(s,'Siete clusters próximos\na cuatro fases',72,330,550,100,32);
    txt(s,'limsup μ < 0,6934',72,465,550,70,44,{bold:true});
    txt(s,'Investigathon 2026',72,615,550,35,24);
    return s;
  }
  if(data.slides.length!==15||data.slides.reduce((a,v)=>a+v.seconds,0)!==900)throw new Error('Invalid talk content');
  if(p.slides.items.length===0)makeCover();
  if(p.slides.items.length!==1)throw new Error('Expected a new canvas or the reviewed cover only');
  for(const d of data.slides.slice(1)){
    const s=p.slides.add();s.background.fill=C.white;
    txt(s,d.title,72,48,1136,74,44,{bold:true});
    txt(s,String(d.slide),1180,671,28,24,17,{color:C.muted,align:'right'});
    const b=d.body;
    if(d.layout==='formula'){
      txt(s,b[0],72,165,1136,70,43);txt(s,b[1],72,260,1136,80,39);
      txt(s,b[2],72,390,1136,80,31);txt(s,b[3],72,505,1136,70,31,{color:C.teal});
    }else if(d.layout==='table'){
      txt(s,b[0],72,158,1136,72,d.slide===6?29:33);
      txt(s,b[1],72,235,1136,54,d.slide===6?33:29,{color:C.teal});
      table(s,d.table,72,315,1136,d.slide===6?260:275,d.slide===6?[240,896]:[420,716],25);
    }else if(d.layout==='quarter'){
      b.slice(0,4).forEach((v,i)=>txt(s,v,72,176+i*78,510,60,31));
      txt(s,b[4],72,570,1136,60,29,{color:C.teal});
      const axis={min:-1.5,max:1.5,majorUnit:1.5,numberFormatCode:'0.0',textStyle:{fontSize:21,fill:C.muted,typeface:FONT},line:{fill:C.grid,width:1},majorGridlines:{fill:C.grid,width:.7}};
      const chart=s.charts.add('scatter',{position:{left:650,top:155,width:550,height:395},scatterOptions:{style:'marker'},
        series:[['A',1,0,C.teal],['B',0,1,C.copper],['C',-1,0,C.ink],['W',0,-1,'#7D8F99']].map(([name,x,y,color])=>({name,xValues:[x],values:[y],marker:{symbol:'circle',size:14,fill:color}})),
        hasLegend:true,legend:{position:'bottom',overlay:false,textStyle:{fontSize:22,fill:C.ink,typeface:FONT}},
        xAxis:{...axis,position:'bottom',tickLabelPosition:'low',title:{text:'cos θ',textStyle:{fontSize:24,fill:C.ink,typeface:FONT}}},
        yAxis:{...axis,position:'left',tickLabelPosition:'low',title:{text:'sin θ',textStyle:{fontSize:24,fill:C.ink,typeface:FONT}}},
        chartFill:C.white,plotAreaFill:C.white,chartLine:{fill:'none',width:0}});
    }else if(d.layout==='statement'){
      txt(s,b[0],72,165,1136,95,61,{bold:true,color:C.teal});
      b.slice(1).forEach((v,i)=>txt(s,v,72,320+i*100,1136,85,32));
    }else if(d.layout==='bound'){
      txt(s,b[0],72,168,1136,90,52,{bold:true,color:C.teal});
      txt(s,b[1],72,310,1136,70,37);txt(s,b[2],72,425,1136,60,36);
      txt(s,b[3],72,545,1136,65,30);
    }else if(d.layout==='identity'){
      txt(s,b[0],72,155,1136,80,27);txt(s,b[1],72,250,1136,70,26,{color:C.muted});
      b.slice(2).forEach((v,i)=>txt(s,v,72,365+i*85,1136,72,31,{color:i===1?C.teal:C.ink,bold:i===1}));
    }else if(d.layout==='parameters'){
      txt(s,b[0],72,160,1136,65,32,{bold:true});txt(s,b[1],72,250,1136,70,36,{color:C.teal});
      txt(s,b[2],72,350,1136,65,29);txt(s,b[3],72,445,1136,65,25);txt(s,b[4],72,535,1136,65,25);
    }else if(d.layout==='mass'){
      txt(s,b[0],72,155,1136,80,54,{bold:true,color:C.teal});
      txt(s,b[1],72,250,1136,55,29);txt(s,b[2],72,315,1136,70,25);
      table(s,d.table,72,415,1136,205,[220,916],26);
    }else if(d.layout==='scale'){
      txt(s,b[0],72,160,1136,70,38);txt(s,b[1],72,255,1136,70,38);
      txt(s,b[2],72,370,1136,80,46,{bold:true,color:C.teal});
      txt(s,b[3],72,485,1136,65,29);txt(s,b[4],72,565,1136,60,28);
    }else if(d.layout==='covering'){
      txt(s,b[0],72,155,1136,65,34,{color:C.teal});
      table(s,d.table,72,250,1136,310,[840,296],28);
      txt(s,b[1],72,585,1136,50,28);
    }else if(d.layout==='checks'){
      b.forEach((v,i)=>txt(s,v,72,160+i*88,1136,78,29,{color:i===4?C.teal:C.ink}));
    }else if(d.layout==='limits'){
      b.forEach((v,i)=>txt(s,v,72,170+i*105,1136,90,i===0?36:31,{bold:i===0,color:i===0?C.teal:C.ink}));
    }else if(d.layout==='closing'){
      txt(s,b[0],72,160,1136,90,61,{bold:true,color:C.teal});
      txt(s,b[1],72,300,1136,105,32);txt(s,b[2],72,445,1136,85,31);
      txt(s,b[3],72,565,1136,65,27,{color:C.muted});
    }else throw new Error('Unknown layout '+d.layout);
    const source=d.slide===5?'O’Keeffe, arXiv:2610.21271v1, IV.3':d.slide===4?'Fases límite. El tamaño de los marcadores no representa masas.':d.slide===7?'Cota superior: cota_flujos_06934.md. Extremo inferior: O’Keeffe v1.':d.sources[0];
    txt(s,source,72,647,1090,25,17,{color:C.muted});
  }
  for(const [i,s]of p.slides.items.entries()){
    const d=data.slides[i];s.speakerNotes.text=`Tiempo objetivo: ${d.seconds} segundos. Sin ensayo medido.\n\n${d.notes}\n\nFuentes:\n${d.sources.join('\n')}`;
  }
  return {slides:p.slides.items.length,targetSeconds:900,nativeTableSlides:[3,6,10,12],nativeChartSlides:[4],rehearsed:false};
}
