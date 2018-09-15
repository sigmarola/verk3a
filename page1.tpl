% include('header.tpl')
% ktSum=[]
% for x in kt:
%   ktSum.append(int(x))
% end
% ktSum = sum(ktSum)
<p>{{kt}}</p>
<p>{{ktSum}}</p>
% include('footer.tpl')
