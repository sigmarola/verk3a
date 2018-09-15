% include('./header')
<header>
          <ul>
          % for x, y in names.items():
           <li><a href="{{y}}">{{x}}</a></li>
          %end
          </ul>
</header>

% include('./footer.tpl')
