replica_idex = {}
replica_bilaxy = {}
replica_hotbit = {}
replica_hitbtc = {}

all_compared_tokens = []
uniswap_prices_set = []

idex_apis = [
    'cddba27a-916f-48e7-bad3-884c0869b627',
    '5e7810c3-bcad-4467-8069-630e52752806',
    '6ae1849c-c8eb-46f8-a735-94b10ddcea2d',
    'faa69304-22a7-48fb-83fd-b5f5a372b758',
    '93872815-45fa-46a7-a1ed-b9d7f2200ec3',
    'd590c3cb-d35d-47dd-b38d-c0b91a124f11',
    '6a59e1d2-691f-4858-bb71-3c9a6297c82f',
    '14936906-d513-444c-8e06-10d53f5f3b3c',
    '5fb56407-582a-4132-9a92-a7e93684e81a',
    '6692e791-a7c6-45f3-9930-6a6c695a5689',
    '4f19b13d-aa3e-48c0-8cfc-9ad17ddc8266',
    '03b8d5fb-89a0-45a7-b615-6a2aa6f8570b',
    '28625e1b-eb3f-4780-97f7-6db1ca4047e6',
    '6bfd2f58-ece3-41fe-af8a-3209a4e6ae55',
    '08288b4c-5a79-47eb-bd23-a29034c80a06',
    '0ec315f5-3fd9-4c75-9b0a-3ae8af0adf9f',
    'cd8052e2-5286-48f8-a33e-873f475de0cd',
    '479e9cb9-d5c8-447f-ae6f-7b4cf38f47e0',
    'b2867fa3-f57a-4749-850a-a0db4217dcc1',
    'a094c2e0-e518-41cb-8992-e9ea225a5bda',
]

# Bilaxy
proxys1 = [
    # IPv4 shopproxy_net
    ['46.8.222.114', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.142.66', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.143.20', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.143.207', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.143.240', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.14.198', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.15.19', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.15.89', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.143.40', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.143.106', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.137.137', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.128.237', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.129.188', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.129.202', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.22.133', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.23.92', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.23.118', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.23.213', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.55.67', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.11.150', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.212.50', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.213.36', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.213.112', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.213.207', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.166.60', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.154.226', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.221.114', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.218.36', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.188.34', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.185.104', '3001', 'sJMRc2b7', 'kb2HxcfV'],
]

# Idex
proxys2 = [
    # IPv4 proxys.io
    ['193.111.154.84', '17097', 'user53105', '3x7cyr'],
    ['185.20.184.161', '17097', 'user53105', '3x7cyr'],
    ['193.111.154.241', '17097', 'user53105', '3x7cyr'],
    ['193.111.152.14', '17097', 'user53105', '3x7cyr'],
    ['193.111.152.87', '17097', 'user53105', '3x7cyr'],
    ['185.161.210.204', '17097', 'user53105', '3x7cyr'],
    ['193.111.152.197', '17097', 'user53105', '3x7cyr'],
    ['193.111.152.89', '17097', 'user53105', '3x7cyr'],
    ['193.111.152.171', '17097', 'user53105', '3x7cyr'],
    ['185.36.189.164', '17097', 'user53105', '3x7cyr'],
    ['147.135.175.226', '11983', 'user53105', '3x7cyr'],
    ['79.137.15.162', '11983', 'user53105', '3x7cyr'],
    ['178.32.67.233', '11983', 'user53105', '3x7cyr'],
    ['178.32.67.182', '11983', 'user53105', '3x7cyr'],
    ['147.135.206.67', '11983', 'user53105', '3x7cyr'],
    ['147.135.206.37', '11983', 'user53105', '3x7cyr'],
    ['213.32.84.41', '11983', 'user53105', '3x7cyr'],
    ['178.32.67.156', '11983', 'user53105', '3x7cyr'],
    ['147.135.206.12', '11983', 'user53105', '3x7cyr'],
    ['149.202.104.8', '11983', 'user53105', '3x7cyr'],
]

# Hitbtc
proxys3 = [
    # IPv4 shopproxy_net
    ['188.130.187.148', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['5.183.130.210', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['45.81.136.216', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['2.59.50.242', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['45.84.177.83', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['45.86.0.36', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['45.87.252.186', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['45.87.253.94', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['185.181.246.10', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['185.181.247.180', '3001', 'sJMRc2b7', 'kb2HxcfV'],
]

# Hotbit
proxys4 = [
    # IPv4 proxys.io
    ['188.130.137.95', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.110.252', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.111.235', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.106.121', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.107.91', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['188.130.128.62', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['188.130.128.208', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.22.109', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['109.248.55.124', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.154.161', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['188.130.218.59', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['188.130.218.242', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.156.139', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['109.248.128.10', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['94.158.190.31', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['45.15.72.3', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['45.81.137.147', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['2.59.50.55', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['45.86.0.17', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['45.87.252.134', '3001', 'OUTmnHk3', 'AfCfzCco'],
]

proxys = [
    # IPv4 proxys.io
    ['193.111.154.84', '17097', 'user53105', '3x7cyr'],
    ['185.20.184.161', '17097', 'user53105', '3x7cyr'],
    ['193.111.154.241', '17097', 'user53105', '3x7cyr'],
    ['193.111.152.14', '17097', 'user53105', '3x7cyr'],
    ['193.111.152.87', '17097', 'user53105', '3x7cyr'],
    ['185.161.210.204', '17097', 'user53105', '3x7cyr'],
    ['193.111.152.197', '17097', 'user53105', '3x7cyr'],
    ['193.111.152.89', '17097', 'user53105', '3x7cyr'],
    ['193.111.152.171', '17097', 'user53105', '3x7cyr'],
    ['185.36.189.164', '17097', 'user53105', '3x7cyr'],
    ['147.135.175.226', '11983', 'user53105', '3x7cyr'],
    ['79.137.15.162', '11983', 'user53105', '3x7cyr'],
    ['178.32.67.233', '11983', 'user53105', '3x7cyr'],
    ['178.32.67.182', '11983', 'user53105', '3x7cyr'],
    ['147.135.206.67', '11983', 'user53105', '3x7cyr'],
    ['147.135.206.37', '11983', 'user53105', '3x7cyr'],
    ['213.32.84.41', '11983', 'user53105', '3x7cyr'],
    ['178.32.67.156', '11983', 'user53105', '3x7cyr'],
    ['147.135.206.12', '11983', 'user53105', '3x7cyr'],
    ['149.202.104.8', '11983', 'user53105', '3x7cyr'],
    # IPv4 shopproxy_net
    ['188.130.137.95', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.110.252', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.111.235', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.106.121', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.107.91', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['188.130.128.62', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['188.130.128.208', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.22.109', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['109.248.55.124', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.154.161', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['188.130.218.59', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['188.130.218.242', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['46.8.156.139', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['109.248.128.10', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['94.158.190.31', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['45.15.72.3', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['45.81.137.147', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['2.59.50.55', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['45.86.0.17', '3001', 'OUTmnHk3', 'AfCfzCco'],
    ['45.87.252.134', '3001', 'OUTmnHk3', 'AfCfzCco'],
    # IPv4 shopproxy_net
    ['46.8.222.114', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.142.66', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.143.20', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.143.207', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.143.240', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.14.198', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.15.19', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.15.89', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.143.40', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.143.106', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.137.137', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.128.237', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.129.188', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.129.202', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.22.133', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.23.92', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.23.118', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.23.213', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.55.67', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.11.150', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.212.50', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.213.36', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.213.112', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.213.207', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['109.248.166.60', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['46.8.154.226', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.221.114', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.218.36', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.188.34', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.185.104', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['188.130.187.148', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['5.183.130.210', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['45.81.136.216', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['2.59.50.242', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['45.84.177.83', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['45.86.0.36', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['45.87.252.186', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['45.87.253.94', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['185.181.246.10', '3001', 'sJMRc2b7', 'kb2HxcfV'],
    ['185.181.247.180', '3001', 'sJMRc2b7', 'kb2HxcfV'],
]
