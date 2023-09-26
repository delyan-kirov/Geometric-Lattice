
RemoveIsoImages := function(GraphList, GraphImage)
local len, i, element;
i := 0;
len := Length(GraphList);
for element in GraphList do
i := i + 1;
if IsIsomorphicGraph(element, GraphImage) then
Remove(GraphList, i);
fi;
od;
return GraphList;
end;

IsoFreeGraphs := [Lattices[1]];

for element in Lattices do
Lattices := RemoveIsoImages(Lattices, element);
Add(IsoFreeGraphs, Lattices[1]);
od;

GraphAutGps := [];
GraphAutSize := [];

for elements in Lattices do
Add(GraphAutGps, AutomorphismGroup(elements));
Add(GraphAutSize, Size(AutomorphismGroup(elements)));
od;

Print(GraphAutSize);
SaveWorkspace("workspace.g");
PrintTo("result.g", Length(Lattices));
quit;
