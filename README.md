<h1>luohualx-awvs 使用指南</h1>
<em>#author:胖胖小飞侠</em><br>
<h2>一、luohualx系列脚本介绍</h2>
<p><strong>luohuxla</strong>为网络安全圈非著名人士、无任何头衔的<strong><em>胖胖小飞侠</em></strong>开发。luohualx-awvs为luohualx系列脚本之一，本着互相学习、互相促进的想法将自用脚本进行开源。本人能力有限，脚本尚存在瑕疵，还请见谅。如有任何意见或建议请与作者联系</p><br>
<p>该脚本仅限学习交流使用，任何非法用途与作者本人无关</p>
<h2>二、用法</h2>
<h3>1、安装模块</h3>
<code>pip install -r requirements.txt</code>
<h3>2、修改配置文件</h3>
<p>修改config目录下的config.conf文件配置，把awvs的url和apikey替换成自己的</p>
<h3>3、常见用法</h3>
<strong>添加单个扫描目标</strong><br>
<code>python luohualx-awvs.py -aot http://www.ttttest.com -ds 资产描述</code><br>
<strong>下载扫描目标样例表</strong><br>
<code>python luohualx-awvs.py -dtc</code><br>
<strong>批量导入扫描目标,支持txt和csv两种格式</strong><br>
<code>python luohualx-awvs.py -f targets.txt</code><br>
<p>注意：单个添加或批量添加扫描目标后都会询问是否直接扫描，选Y/y/YES/yes都会直接开启扫描任务,其他任意输入则终止脚本</p><br>
<p>扫描完成后需要先生成扫描的报告，生成报告需要一定的时间，等全部生成后再进行下载报告的操作</p><br>
