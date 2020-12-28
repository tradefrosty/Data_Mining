{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Jacob Woodhouse\n",
    "\n",
    "import networkx as nx\n",
    "import matplotlib as plt\n",
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('stack_overflow_edgelist.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>source</th>\n",
       "      <th>target</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>azure</td>\n",
       "      <td>.net</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>sql-server</td>\n",
       "      <td>.net</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>asp.net</td>\n",
       "      <td>.net</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>entity-framework</td>\n",
       "      <td>.net</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>wpf</td>\n",
       "      <td>.net</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>485</th>\n",
       "      <td>objective-c</td>\n",
       "      <td>xcode</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>486</th>\n",
       "      <td>swift</td>\n",
       "      <td>xcode</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>487</th>\n",
       "      <td>iphone</td>\n",
       "      <td>xcode</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>488</th>\n",
       "      <td>ios</td>\n",
       "      <td>xcode</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>489</th>\n",
       "      <td>json</td>\n",
       "      <td>xml</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>490 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               source target\n",
       "0               azure   .net\n",
       "1          sql-server   .net\n",
       "2             asp.net   .net\n",
       "3    entity-framework   .net\n",
       "4                 wpf   .net\n",
       "..                ...    ...\n",
       "485       objective-c  xcode\n",
       "486             swift  xcode\n",
       "487            iphone  xcode\n",
       "488               ios  xcode\n",
       "489              json    xml\n",
       "\n",
       "[490 rows x 2 columns]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "graph = nx.Graph()\n",
    "G = nx.from_pandas_edgelist(df, create_using=graph)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "NodeView(('azure', '.net', 'sql-server', 'asp.net', 'entity-framework', 'wpf', 'linq', 'wcf', 'c#', 'tdd', 'agile', 'codeigniter', 'ajax', 'jquery', 'mysql', 'css', 'php', 'javascript', 'json', 'cloud', 'amazon-web-services', 'devops', 'docker', 'ios', 'android', 'android-studio', 'java', 'typescript', 'angular', 'angular2', 'angularjs', 'ionic-framework', 'reactjs', 'mongodb', 'sass', 'twitter-bootstrap', 'express', 'node.js', 'asp.net-web-api', 'html5', 'nginx', 'apache', 'linux', 'scala', 'apache-spark', 'hadoop', 'rest', 'api', 'sql', 'mvc', 'vb.net', 'bash', 'shell', 'git', 'bootstrap', 'c++', 'c', 'python', 'embedded', 'xamarin', 'unity3d', 'visual-studio', 'qt', 'laravel', 'wordpress', 'photoshop', 'html', 'less', 'jenkins', 'django', 'flask', 'postgresql', 'go', 'drupal', 'maven', 'eclipse', 'redis', 'elasticsearch', 'vba', 'excel', 'excel-vba', 'redux', 'github', 'haskell', 'jsp', 'hibernate', 'spring-boot', 'web-services', 'spring-mvc', 'java-ee', 'spring', 'twitter-bootstrap-3', 'swift', 'osx', 'objective-c', 'iphone', 'xcode', 'xml', 'vue.js', 'unix', 'ubuntu', 'windows', 'machine-learning', 'r', 'matlab', 'react-native', 'oracle', 'plsql', 'regex', 'perl', 'ruby-on-rails', 'ruby', 'powershell', 'testing', 'selenium'))"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "graph.nodes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "EdgeView([('azure', '.net'), ('azure', 'amazon-web-services'), ('azure', 'asp.net'), ('azure', 'asp.net-web-api'), ('azure', 'c#'), ('.net', 'sql-server'), ('.net', 'asp.net'), ('.net', 'entity-framework'), ('.net', 'wpf'), ('.net', 'linq'), ('.net', 'wcf'), ('.net', 'c#'), ('sql-server', 'asp.net'), ('sql-server', 'asp.net-web-api'), ('sql-server', 'c#'), ('sql-server', 'entity-framework'), ('sql-server', 'linq'), ('sql-server', 'sql'), ('sql-server', 'wcf'), ('sql-server', 'vb.net'), ('asp.net', 'sql'), ('asp.net', 'c#'), ('asp.net', 'asp.net-web-api'), ('asp.net', 'jquery'), ('asp.net', 'entity-framework'), ('asp.net', 'mvc'), ('asp.net', 'wpf'), ('asp.net', 'linq'), ('asp.net', 'wcf'), ('asp.net', 'vb.net'), ('entity-framework', 'asp.net-web-api'), ('entity-framework', 'c#'), ('entity-framework', 'wpf'), ('entity-framework', 'linq'), ('entity-framework', 'wcf'), ('wpf', 'c#'), ('wpf', 'linq'), ('wpf', 'wcf'), ('linq', 'c#'), ('linq', 'wcf'), ('wcf', 'asp.net-web-api'), ('wcf', 'c#'), ('c#', 'asp.net-web-api'), ('c#', 'sql'), ('c#', 'vb.net'), ('c#', 'xamarin'), ('c#', 'unity3d'), ('c#', 'visual-studio'), ('tdd', 'agile'), ('codeigniter', 'ajax'), ('codeigniter', 'mysql'), ('codeigniter', 'jquery'), ('codeigniter', 'laravel'), ('codeigniter', 'php'), ('codeigniter', 'wordpress'), ('ajax', 'jquery'), ('ajax', 'mysql'), ('ajax', 'css'), ('ajax', 'php'), ('ajax', 'javascript'), ('ajax', 'json'), ('jquery', 'angularjs'), ('jquery', 'bootstrap'), ('jquery', 'css'), ('jquery', 'html'), ('jquery', 'html5'), ('jquery', 'javascript'), ('jquery', 'json'), ('jquery', 'wordpress'), ('jquery', 'sass'), ('jquery', 'php'), ('jquery', 'twitter-bootstrap'), ('jquery', 'mysql'), ('jquery', 'twitter-bootstrap-3'), ('mysql', 'apache'), ('mysql', 'css'), ('mysql', 'html'), ('mysql', 'javascript'), ('mysql', 'laravel'), ('mysql', 'mongodb'), ('mysql', 'php'), ('mysql', 'postgresql'), ('css', 'angularjs'), ('css', 'bootstrap'), ('css', 'photoshop'), ('css', 'html'), ('css', 'javascript'), ('css', 'html5'), ('css', 'twitter-bootstrap'), ('css', 'less'), ('css', 'wordpress'), ('css', 'sass'), ('css', 'php'), ('php', 'html'), ('php', 'html5'), ('php', 'javascript'), ('php', 'laravel'), ('php', 'wordpress'), ('javascript', 'angularjs'), ('javascript', 'html'), ('javascript', 'html5'), ('javascript', 'twitter-bootstrap'), ('javascript', 'node.js'), ('javascript', 'reactjs'), ('javascript', 'sass'), ('json', 'rest'), ('json', 'xml'), ('cloud', 'amazon-web-services'), ('amazon-web-services', 'devops'), ('amazon-web-services', 'docker'), ('devops', 'docker'), ('devops', 'jenkins'), ('docker', 'go'), ('docker', 'jenkins'), ('ios', 'android'), ('ios', 'swift'), ('ios', 'osx'), ('ios', 'objective-c'), ('ios', 'iphone'), ('ios', 'xcode'), ('android', 'android-studio'), ('android', 'java'), ('java', 'c'), ('java', 'c++'), ('java', 'hibernate'), ('java', 'spring'), ('java', 'jsp'), ('java', 'java-ee'), ('java', 'spring-mvc'), ('typescript', 'angular'), ('typescript', 'angular2'), ('angular2', 'angularjs'), ('angularjs', 'ionic-framework'), ('angularjs', 'reactjs'), ('angularjs', 'mongodb'), ('angularjs', 'sass'), ('angularjs', 'twitter-bootstrap'), ('angularjs', 'express'), ('angularjs', 'node.js'), ('angularjs', 'asp.net-web-api'), ('angularjs', 'html5'), ('reactjs', 'express'), ('reactjs', 'mongodb'), ('reactjs', 'node.js'), ('reactjs', 'react-native'), ('reactjs', 'sass'), ('reactjs', 'redux'), ('mongodb', 'elasticsearch'), ('mongodb', 'express'), ('mongodb', 'node.js'), ('mongodb', 'postgresql'), ('mongodb', 'redis'), ('sass', 'html'), ('sass', 'html5'), ('sass', 'less'), ('sass', 'twitter-bootstrap'), ('twitter-bootstrap', 'html5'), ('express', 'redux'), ('express', 'node.js'), ('node.js', 'react-native'), ('node.js', 'redux'), ('html5', 'wordpress'), ('html5', 'less'), ('html5', 'twitter-bootstrap-3'), ('nginx', 'apache'), ('nginx', 'linux'), ('nginx', 'redis'), ('apache', 'linux'), ('linux', 'bash'), ('linux', 'git'), ('linux', 'unix'), ('linux', 'osx'), ('linux', 'ubuntu'), ('linux', 'shell'), ('linux', 'windows'), ('linux', 'python'), ('scala', 'apache-spark'), ('scala', 'hadoop'), ('scala', 'haskell'), ('apache-spark', 'hadoop'), ('rest', 'api'), ('rest', 'hibernate'), ('rest', 'spring'), ('rest', 'web-services'), ('sql', 'oracle'), ('sql', 'plsql'), ('bash', 'shell'), ('bash', 'git'), ('git', 'jenkins'), ('git', 'github'), ('c++', 'c'), ('c++', 'qt'), ('c++', 'python'), ('c', 'python'), ('c', 'embedded'), ('python', 'django'), ('python', 'flask'), ('python', 'machine-learning'), ('python', 'r'), ('laravel', 'vue.js'), ('wordpress', 'drupal'), ('jenkins', 'maven'), ('django', 'flask'), ('django', 'postgresql'), ('postgresql', 'redis'), ('postgresql', 'ruby-on-rails'), ('postgresql', 'ruby'), ('maven', 'eclipse'), ('maven', 'hibernate'), ('maven', 'spring-mvc'), ('maven', 'spring'), ('redis', 'elasticsearch'), ('vba', 'excel'), ('vba', 'excel-vba'), ('excel', 'excel-vba'), ('redux', 'react-native'), ('jsp', 'hibernate'), ('jsp', 'spring-mvc'), ('jsp', 'spring'), ('hibernate', 'spring-boot'), ('hibernate', 'web-services'), ('hibernate', 'spring-mvc'), ('hibernate', 'java-ee'), ('hibernate', 'spring'), ('spring-boot', 'spring'), ('spring-boot', 'spring-mvc'), ('web-services', 'spring'), ('spring-mvc', 'java-ee'), ('spring-mvc', 'spring'), ('java-ee', 'spring'), ('swift', 'iphone'), ('swift', 'objective-c'), ('swift', 'xcode'), ('osx', 'objective-c'), ('osx', 'windows'), ('objective-c', 'iphone'), ('objective-c', 'xcode'), ('iphone', 'xcode'), ('windows', 'powershell'), ('machine-learning', 'r'), ('r', 'matlab'), ('oracle', 'plsql'), ('regex', 'perl'), ('ruby-on-rails', 'ruby'), ('testing', 'selenium')])"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "graph.edges"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of Nodes: 115\n",
      "Number of Edges: 245\n"
     ]
    }
   ],
   "source": [
    "print('Number of Nodes: {}'.format(graph.number_of_nodes()))\n",
    "print('Number of Edges: {}'.format(graph.number_of_edges()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "pr = nx.pagerank(graph, alpha=.9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'azure': 0.008636678605772745,\n",
       " '.net': 0.011950574726124735,\n",
       " 'sql-server': 0.013568239091009848,\n",
       " 'asp.net': 0.019792633756092727,\n",
       " 'entity-framework': 0.011785719753713673,\n",
       " 'wpf': 0.009029367441243549,\n",
       " 'linq': 0.010402945773182015,\n",
       " 'wcf': 0.011785719753713673,\n",
       " 'c#': 0.02265714933828647,\n",
       " 'tdd': 0.008695652173913044,\n",
       " 'agile': 0.008695652173913044,\n",
       " 'codeigniter': 0.009354024750882532,\n",
       " 'ajax': 0.010667104867694274,\n",
       " 'jquery': 0.023352079507991515,\n",
       " 'mysql': 0.017162629615073036,\n",
       " 'css': 0.020662198202053658,\n",
       " 'php': 0.01467848767896036,\n",
       " 'javascript': 0.01705797818483871,\n",
       " 'json': 0.007773997943679374,\n",
       " 'cloud': 0.0030946685012798745,\n",
       " 'amazon-web-services': 0.009888110676897535,\n",
       " 'devops': 0.007687493946359192,\n",
       " 'docker': 0.010539941363777785,\n",
       " 'ios': 0.013014516729856242,\n",
       " 'android': 0.0074490807286526585,\n",
       " 'android-studio': 0.0031044457214924473,\n",
       " 'java': 0.016291851299802367,\n",
       " 'typescript': 0.0068235586126142445,\n",
       " 'angular': 0.003937173161461651,\n",
       " 'angular2': 0.005343278716021672,\n",
       " 'angularjs': 0.02031561720808745,\n",
       " 'ionic-framework': 0.0022756707719513254,\n",
       " 'reactjs': 0.01228505382389467,\n",
       " 'mongodb': 0.013521209060661746,\n",
       " 'sass': 0.01297668247093833,\n",
       " 'twitter-bootstrap': 0.008807257506153795,\n",
       " 'express': 0.008086982104115032,\n",
       " 'node.js': 0.010960416419723493,\n",
       " 'asp.net-web-api': 0.010664996595144171,\n",
       " 'html5': 0.014595499626656266,\n",
       " 'nginx': 0.006876785987314159,\n",
       " 'apache': 0.006537083033075656,\n",
       " 'linux': 0.024441964235935722,\n",
       " 'scala': 0.012861655533522563,\n",
       " 'apache-spark': 0.008596455304092847,\n",
       " 'hadoop': 0.008596455304092847,\n",
       " 'rest': 0.010351118982384097,\n",
       " 'api': 0.002732760704091121,\n",
       " 'sql': 0.009178532258877537,\n",
       " 'mvc': 0.0022396967778433095,\n",
       " 'vb.net': 0.005052801418267962,\n",
       " 'bash': 0.007901587047551345,\n",
       " 'shell': 0.0054406677631132485,\n",
       " 'git': 0.01058949047740472,\n",
       " 'bootstrap': 0.00351105825609267,\n",
       " 'c++': 0.010009052707764863,\n",
       " 'c': 0.010009052707764863,\n",
       " 'python': 0.017450528274522557,\n",
       " 'embedded': 0.003121924174899087,\n",
       " 'xamarin': 0.0023259748514813656,\n",
       " 'unity3d': 0.0023259748514813656,\n",
       " 'visual-studio': 0.0023259748514813656,\n",
       " 'qt': 0.003121924174899087,\n",
       " 'laravel': 0.007247254952817831,\n",
       " 'wordpress': 0.009630605584310812,\n",
       " 'photoshop': 0.002197674921826388,\n",
       " 'html': 0.008812685424734653,\n",
       " 'less': 0.004808591762854737,\n",
       " 'jenkins': 0.009869328677604835,\n",
       " 'django': 0.007350376001902876,\n",
       " 'flask': 0.005319072089576208,\n",
       " 'postgresql': 0.012284604550929092,\n",
       " 'go': 0.0032414356913277754,\n",
       " 'drupal': 0.002313937731082493,\n",
       " 'maven': 0.01076685220974697,\n",
       " 'eclipse': 0.002807749336710113,\n",
       " 'redis': 0.008203048069115757,\n",
       " 'elasticsearch': 0.0042364013819708,\n",
       " 'vba': 0.008695652173913044,\n",
       " 'excel': 0.008695652173913044,\n",
       " 'excel-vba': 0.008695652173913044,\n",
       " 'redux': 0.006663914507934208,\n",
       " 'github': 0.0032526592138767117,\n",
       " 'haskell': 0.004728042553943909,\n",
       " 'jsp': 0.007851763908001897,\n",
       " 'hibernate': 0.01712707458693977,\n",
       " 'spring-boot': 0.006018779033657336,\n",
       " 'web-services': 0.006158322063214491,\n",
       " 'spring-mvc': 0.013405474948657257,\n",
       " 'java-ee': 0.007851763908001895,\n",
       " 'spring': 0.01712707458693977,\n",
       " 'twitter-bootstrap-3': 0.0034963683661039416,\n",
       " 'swift': 0.008662992562522134,\n",
       " 'osx': 0.00941938855783058,\n",
       " 'objective-c': 0.010789667226481357,\n",
       " 'iphone': 0.008662992562522134,\n",
       " 'xcode': 0.008662992562522136,\n",
       " 'xml': 0.0026185643422792326,\n",
       " 'vue.js': 0.0025000176684403575,\n",
       " 'unix': 0.0030697327050136967,\n",
       " 'ubuntu': 0.0030697327050136967,\n",
       " 'windows': 0.00818184180428597,\n",
       " 'machine-learning': 0.0057860495970994035,\n",
       " 'r': 0.008906264958932306,\n",
       " 'matlab': 0.0035419780134333377,\n",
       " 'react-native': 0.005159788231087132,\n",
       " 'oracle': 0.004584441825017182,\n",
       " 'plsql': 0.004584441825017182,\n",
       " 'regex': 0.008695652173913044,\n",
       " 'perl': 0.008695652173913044,\n",
       " 'ruby-on-rails': 0.004931664580289447,\n",
       " 'ruby': 0.004931664580289446,\n",
       " 'powershell': 0.003324504349113993,\n",
       " 'testing': 0.008695652173913044,\n",
       " 'selenium': 0.008695652173913044}"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Top 10 Ranked Nodes\n",
      "linux 0.024441964235935722\n",
      "jquery 0.023352079507991515\n",
      "c# 0.02265714933828647\n",
      "css 0.020662198202053658\n",
      "angularjs 0.02031561720808745\n",
      "asp.net 0.019792633756092727\n",
      "python 0.017450528274522557\n",
      "mysql 0.017162629615073036\n",
      "hibernate 0.01712707458693977\n",
      "spring 0.01712707458693977\n"
     ]
    }
   ],
   "source": [
    "print(\"The Top 10 Ranked Nodes\")\n",
    "\n",
    "sorted_pr = sorted(pr.items(), key=lambda x: x[1], reverse=True)\n",
    "count = 0;\n",
    "for i in sorted_pr:\n",
    "    print(i[0], i[1])\n",
    "    count += 1\n",
    "    if count == 10:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Bottom 10 Ranked Nodes\n",
      "photoshop 0.002197674921826388\n",
      "mvc 0.0022396967778433095\n",
      "ionic-framework 0.0022756707719513254\n",
      "drupal 0.002313937731082493\n",
      "xamarin 0.0023259748514813656\n",
      "unity3d 0.0023259748514813656\n",
      "visual-studio 0.0023259748514813656\n",
      "vue.js 0.0025000176684403575\n",
      "xml 0.0026185643422792326\n",
      "api 0.002732760704091121\n"
     ]
    }
   ],
   "source": [
    "print(\"The Bottom 10 Ranked Nodes\")\n",
    "\n",
    "sorted_pr = sorted(pr.items(), key=lambda x: x[1], reverse=False)\n",
    "count = 0;\n",
    "for i in sorted_pr:\n",
    "    print(i[0], i[1])\n",
    "    count += 1\n",
    "    if count == 10:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
