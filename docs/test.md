<div id="container">

<div class="section">

<div class="docs">

# application.py

</div>

</div>

<div class="clearall">

<div class="section" id="section-0">

<div class="docs">

<div class="octowrap">[#](#section-0)</div>

</div>

<div class="code">

<div class="highlight">

<pre><span></span><span class="n">__author__</span> <span class="o">=</span> <span class="s1">'Dmitriy.Dakhnovskiy'</span>

<span class="kn">from</span> <span class="nn">request.request</span> <span class="kn">import</span> <span class="n">Request</span>
<span class="kn">from</span> <span class="nn">response.response</span> <span class="kn">import</span> <span class="n">Response</span></pre>

</div>

</div>

</div>

<div class="section" id="section-1">

<div class="docs">

<div class="octowrap">[#](#section-1)</div>

Класс web-приложение

</div>

<div class="code">

<div class="highlight">

<pre><span class="k">class</span> <span class="nc">Application</span><span class="p">:</span></pre>

</div>

</div>

</div>

<div class="section" id="section-2">

<div class="docs">

<div class="octowrap">[#](#section-2)</div>

</div>

</div>

<div class="section" id="section-3">

<div class="docs">

<div class="octowrap">[#](#section-3)</div>

</div>

<div class="code">

<div class="highlight">

<pre>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">__routing_map</span> <span class="o">=</span> <span class="p">{}</span></pre>

</div>

</div>

</div>

<div class="section" id="section-4">

<div class="docs">

<div class="octowrap">[#](#section-4)</div>

:param environ: словарь - окружение приходящее в application из uWSGI :param start_response: callable - объект переданный uWSGI :return: тело ответа

</div>

<div class="code">

<div class="highlight">

<pre>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">environ</span><span class="p">,</span> <span class="n">start_response</span><span class="p">):</span></pre>

</div>

</div>

</div>

<div class="section" id="section-5">

<div class="docs">

<div class="octowrap">[#](#section-5)</div>

</div>

<div class="code">

<div class="highlight">

<pre>        <span class="n">requset</span> <span class="o">=</span> <span class="n">Request</span><span class="p">(</span><span class="n">environ</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__get_response_function</span><span class="p">(</span><span class="n">requset</span><span class="o">.</span><span class="n">path_info</span><span class="p">)(</span><span class="n">requset</span><span class="p">)</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">Response</span><span class="p">),</span> <span class="s1">'response must be Response'</span>
        <span class="k">return</span> <span class="n">response</span><span class="p">(</span><span class="n">start_response</span><span class="p">)</span></pre>

</div>

</div>

</div>

<div class="section" id="section-6">

<div class="docs">

<div class="octowrap">[#](#section-6)</div>

Получить функцию-ответ по path_info :param path_info: Остаток пути в URL соответствующий цели запроса внутри приложения :return: функция

</div>

<div class="code">

<div class="highlight">

<pre>    <span class="k">def</span> <span class="nf">__get_response_function</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_info</span><span class="p">):</span></pre>

</div>

</div>

</div>

<div class="section" id="section-7">

<div class="docs">

<div class="octowrap">[#](#section-7)</div>

</div>

<div class="code">

<div class="highlight">

<pre>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__routing_map</span><span class="p">[</span><span class="n">path_info</span><span class="p">]</span></pre>

</div>

</div>

</div>

<div class="section" id="section-8">

<div class="docs">

<div class="octowrap">[#](#section-8)</div>

Добавить функцию-ответ соответствующую path_info :param path_info: Остаток пути в URL соответствующий цели запроса внутри приложения :param response_function: функция-ответ

</div>

<div class="code">

<div class="highlight">

<pre>    <span class="k">def</span> <span class="nf">add_response_function</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_info</span><span class="p">,</span> <span class="n">response_function</span><span class="p">):</span></pre>

</div>

</div>

</div>

<div class="section" id="section-9">

<div class="docs">

<div class="octowrap">[#](#section-9)</div>

</div>

</div>

<div class="section" id="section-10">

<div class="docs">

<div class="octowrap">[#](#section-10)</div>

TODO: exception for 404

</div>

<div class="code">

<div class="highlight">

<pre>        <span class="bp">self</span><span class="o">.</span><span class="n">__routing_map</span><span class="p">[</span><span class="n">path_info</span><span class="p">]</span> <span class="o">=</span> <span class="n">response_function</span></pre>

</div>

</div>

</div>

<div class="section" id="section-11">

<div class="docs">

<div class="octowrap">[#](#section-11)</div>

Метод возвращающий декоратор для регистрации функций-ответов

</div>

<div class="code">

<div class="highlight">

<pre>    <span class="k">def</span> <span class="nf">route</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_info</span><span class="p">):</span></pre>

</div>

</div>

</div>

<div class="section" id="section-12">

<div class="docs">

<div class="octowrap">[#](#section-12)</div>

</div>

<div class="code">

<div class="highlight">

<pre>        <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">response_function</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">add_response_function</span><span class="p">(</span><span class="n">path_info</span><span class="p">,</span> <span class="n">response_function</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">response_function</span>
        <span class="k">return</span> <span class="n">decorator</span>

</pre>

</div>

</div>

</div>

</div>

</div>