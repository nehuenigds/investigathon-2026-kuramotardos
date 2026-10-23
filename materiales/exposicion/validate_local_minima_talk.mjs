// Invoke inside artifactSession.run. Checks the live editable objects against
// the review source and preserved native reference, without exporting a PPTX.
export function validateLocalMinimaTalk(p, data, reference, coverage) {
  const fail=message=>{throw new Error(message);};
  const current=p.toProto();
  const report={slides:p.slides.items.length,targetSeconds:data.slides.reduce((n,s)=>n+s.seconds,0),
    allBodyTextMatches:true,allSpeakerNotesMatch:true,allNativeTableValuesMatch:true,
    allSlideIDsPreserved:true,allElementIDsPreserved:true,outOfCanvasObjects:[],
    nativeTableSlides:[],nativeChartSlides:[],
    originalChartProtoUnchanged:JSON.stringify(current.charts)===JSON.stringify(reference.charts),
    originalImageProtoUnchanged:JSON.stringify(current.images)===JSON.stringify(reference.images)};
  if(report.slides!==15||data.slides.length!==15||report.targetSeconds!==900)fail('Slide count or target timing mismatch');
  for(let i=0;i<15;i++){
    const s=p.slides.items[i],d=data.slides[i],before=reference.slides[i],now=current.slides[i];
    report.allSlideIDsPreserved=report.allSlideIDsPreserved&&s.id===before.id;
    report.allElementIDsPreserved=report.allElementIDsPreserved&&JSON.stringify(now.elements.map(v=>v.id))===JSON.stringify(before.elements.map(v=>v.id));
    if(now.widthEmu!==before.widthEmu||now.heightEmu!==before.heightEmu)fail('Changed reference slide size');
    if(i){report.allBodyTextMatches=report.allBodyTextMatches&&s.shapes.items[0].text.toString()===d.title&&d.body.every((text,k)=>s.shapes.items[k+2].text.toString()===text);}
    report.allSpeakerNotesMatch=report.allSpeakerNotesMatch&&s.speakerNotes.text===`Tiempo objetivo: ${d.seconds} segundos. Sin ensayo medido.\n\n${d.notes}\n\nFuentes:\n${d.sources.join('\n')}`;
    if(d.table){report.allNativeTableValuesMatch=report.allNativeTableValuesMatch&&d.table.every((row,r)=>row.every((text,c)=>s.tables.items[0].getCell(r,c).text.toString()===text));}
    if(s.tables.items.length)report.nativeTableSlides.push(i+1);
    if(s.charts.items.length)report.nativeChartSlides.push(i+1);
    for(const [kind,items] of [['shape',s.shapes.items],['table',s.tables.items],['chart',s.charts.items],['image',s.images.items]])for(const object of items){
      const q=object.position;
      if(q.left<-.1||q.top<-.1||q.left+q.width>1280.1||q.top+q.height>720.1)report.outOfCanvasObjects.push({slide:i+1,kind,id:object.id});
    }
  }
  if(!p.slides.items[0].shapes.items.some(s=>s.text.toString().includes('Los Kuramotardos')))fail('Team name missing');
  if(!p.slides.items[5].tables.items[0].getCell(3,1).text.toString().includes('Mínimo local'))fail('Expanded hypothesis missing');
  if(!data.slides[7].sources.some(v=>v.includes('Lepsveridze')))fail('Cubic descent attribution missing');
  if(coverage.target!=='3467/5000'||!coverage.all_leaves_verified)fail('Wrong coverage report');
  const c=coverage.counts;
  const grouped=c.capacity+c.mass_flow_upper+c.mass_flow_sum+c.whole_mass_projection+c.aggregate_cut+c.central_mass_projection+c.variance_scale;
  const visible=data.slides[11].table.slice(1).map(row=>Number(row[1].replaceAll('.','')));
  if(JSON.stringify(visible)!==JSON.stringify([grouped,c.matrix,c.bernstein_matrix,grouped+c.matrix+c.bernstein_matrix]))fail('Certificate counts and native table differ');
  report.coverageCountsMatch=true;
  report.nativeChartValues={A:[1,0],B:[0,1],C:[-1,0],W:[0,-1]};
  for(const key of ['allBodyTextMatches','allSpeakerNotesMatch','allNativeTableValuesMatch','allSlideIDsPreserved','allElementIDsPreserved','originalChartProtoUnchanged','originalImageProtoUnchanged'])if(!report[key])fail(key);
  if(report.outOfCanvasObjects.length)fail('Object outside canvas');
  if(JSON.stringify(report.nativeTableSlides)!==JSON.stringify([3,6,10,12])||JSON.stringify(report.nativeChartSlides)!==JSON.stringify([4]))fail('Native evidence owners changed');
  return report;
}
