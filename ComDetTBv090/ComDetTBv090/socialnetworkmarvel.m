xy = [Gh.Nodes.XCoord Gh.Nodes.YCoord];
[s,t] = findedge(Gh);
Gh.Edges.Weight = hypot(xy(s,1)-xy(t,1), xy(s,2)-xy(t,2));
p = plot(Gh,'XData',xy(:,1),'YData',xy(:,2),'MarkerSize',5);
title('Minnesota Road Network')
ucc = centrality(Gh,'betweenness');
p.NodeCData = ucc;
colormap jet
colorbar
title('Closeness Centrality Scores - Unweighted')
wcc = centrality(Gh,'Closeness','Cost',Gh.Edges.Weight);
p.NodeCData = wcc;
title('Closeness Centrality Scores - Weighted')
% wbc = centrality(Gh,'degree','Cost',Gh.Edges.Weight);
% n = numnodes(Gh);
% p.NodeCData = 2*wbc./((n-2)*(n-1));
% colormap(flip(autumn,1));
% title('Betweenness Centrality Scores - Weighted')