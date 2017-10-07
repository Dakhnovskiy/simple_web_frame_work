{::nomarkdown}
<!-- HTML CODE-->

<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html;charset=utf-8">
  <title>application.py</title>
  <link rel="stylesheet" href="pycco.css">
</head>
<body>
<div id='container'>
  <div id="background"></div>
  <div class='section'>
    <div class='docs'><h1>application.py</h1></div>
  </div>
  <div class='clearall'>
  <div class='section' id='section-0'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-0'>#</a>
      </div>
      
    </div>
    <div class='code'>
      <div class="highlight"><pre><span></span><span class="n">__author__</span> <span class="o">=</span> <span class="s1">&#39;Dmitriy.Dakhnovskiy&#39;</span>

<span class="kn">from</span> <span class="nn">request.request</span> <span class="kn">import</span> <span class="n">Request</span>
<span class="kn">from</span> <span class="nn">response.response</span> <span class="kn">import</span> <span class="n">Response</span></pre></div>
    </div>
  </div>
  <div class='clearall'></div>
  <div class='section' id='section-1'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-1'>#</a>
      </div>
      <p>Класс web-приложение</p>
    </div>
    <div class='code'>
      <div class="highlight"><pre><span class="k">class</span> <span class="nc">Application</span><span class="p">:</span></pre></div>
    </div>
  </div>
  <div class='clearall'></div>
  <div class='section' id='section-2'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-2'>#</a>
      </div>
      
    </div>
    <div class='code'>
      <div class="highlight"><pre></pre></div>
    </div>
  </div>
  <div class='clearall'></div>
  <div class='section' id='section-3'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-3'>#</a>
      </div>
      
    </div>
    <div class='code'>
      <div class="highlight"><pre>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">__routing_map</span> <span class="o">=</span> <span class="p">{}</span></pre></div>
    </div>
  </div>
  <div class='clearall'></div>
  <div class='section' id='section-4'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-4'>#</a>
      </div>
      <p>:param environ: словарь - окружение приходящее в application из uWSGI
:param start_response: callable - объект переданный uWSGI
:return: тело ответа</p>
    </div>
    <div class='code'>
      <div class="highlight"><pre>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">environ</span><span class="p">,</span> <span class="n">start_response</span><span class="p">):</span></pre></div>
    </div>
  </div>
  <div class='clearall'></div>
  <div class='section' id='section-5'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-5'>#</a>
      </div>
      
    </div>
    <div class='code'>
      <div class="highlight"><pre>        <span class="n">requset</span> <span class="o">=</span> <span class="n">Request</span><span class="p">(</span><span class="n">environ</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__get_response_function</span><span class="p">(</span><span class="n">requset</span><span class="o">.</span><span class="n">path_info</span><span class="p">)(</span><span class="n">requset</span><span class="p">)</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">Response</span><span class="p">),</span> <span class="s1">&#39;response must be Response&#39;</span>
        <span class="k">return</span> <span class="n">response</span><span class="p">(</span><span class="n">start_response</span><span class="p">)</span></pre></div>
    </div>
  </div>
  <div class='clearall'></div>
  <div class='section' id='section-6'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-6'>#</a>
      </div>
      <p>Получить функцию-ответ по path_info
:param path_info: Остаток пути в URL соответствующий цели запроса внутри приложения
:return: функция</p>
    </div>
    <div class='code'>
      <div class="highlight"><pre>    <span class="k">def</span> <span class="nf">__get_response_function</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_info</span><span class="p">):</span></pre></div>
    </div>
  </div>
  <div class='clearall'></div>
  <div class='section' id='section-7'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-7'>#</a>
      </div>
      
    </div>
    <div class='code'>
      <div class="highlight"><pre>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__routing_map</span><span class="p">[</span><span class="n">path_info</span><span class="p">]</span></pre></div>
    </div>
  </div>
  <div class='clearall'></div>
  <div class='section' id='section-8'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-8'>#</a>
      </div>
      <p>Добавить функцию-ответ соответствующую path_info
:param path_info: Остаток пути в URL соответствующий цели запроса внутри приложения
:param response_function: функция-ответ</p>
    </div>
    <div class='code'>
      <div class="highlight"><pre>    <span class="k">def</span> <span class="nf">add_response_function</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_info</span><span class="p">,</span> <span class="n">response_function</span><span class="p">):</span></pre></div>
    </div>
  </div>
  <div class='clearall'></div>
  <div class='section' id='section-9'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-9'>#</a>
      </div>
      
    </div>
    <div class='code'>
      <div class="highlight"><pre></pre></div>
    </div>
  </div>
  <div class='clearall'></div>
  <div class='section' id='section-10'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-10'>#</a>
      </div>
      <p>TODO: exception for 404</p>
    </div>
    <div class='code'>
      <div class="highlight"><pre>        <span class="bp">self</span><span class="o">.</span><span class="n">__routing_map</span><span class="p">[</span><span class="n">path_info</span><span class="p">]</span> <span class="o">=</span> <span class="n">response_function</span></pre></div>
    </div>
  </div>
  <div class='clearall'></div>
  <div class='section' id='section-11'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-11'>#</a>
      </div>
      <p>Метод возвращающий декоратор для регистрации функций-ответов</p>
    </div>
    <div class='code'>
      <div class="highlight"><pre>    <span class="k">def</span> <span class="nf">route</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_info</span><span class="p">):</span></pre></div>
    </div>
  </div>
  <div class='clearall'></div>
  <div class='section' id='section-12'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-12'>#</a>
      </div>
      
    </div>
    <div class='code'>
      <div class="highlight"><pre>        <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">response_function</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">add_response_function</span><span class="p">(</span><span class="n">path_info</span><span class="p">,</span> <span class="n">response_function</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">response_function</span>
        <span class="k">return</span> <span class="n">decorator</span>

</pre></div>
    </div>
  </div>
  <div class='clearall'></div>
</div>
</body>
{:/}