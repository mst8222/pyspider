# pyspider - Python 网络爬虫

Python 编写的通用网络爬虫，采用模块化架构，包含 URL 管理、页面下载、HTML 解析、数据输出等完整流程。支持百度百科等网站的内容抓取。

## 功能特点

- 🕷️ **通用爬虫框架**：支持多类型网站的内容抓取
- 📄 **HTML 解析**：支持百度百科等结构化页面的解析
- 🔗 **URL 管理**：自动发现新链接，支持去重
- 📊 **数据输出**：结构化数据输出到 HTML 或控制台

## 架构模块

```
pyspider/
├── spider_main.py      # 爬虫主入口，协调各模块
├── url_manager.py      # URL 管理（待爬取/已爬取）
├── html_downloader.py  # 页面下载器
├── html_paser.py       # HTML 解析器（BeautifulSoup）
├── html_outputer.py    # 数据输出器
├── baike_spider/       # 百度百科爬虫示例
└── test/               # 测试用例
```

## 技术栈

- Python 3
- urllib
- BeautifulSoup4

## 快速开始

```bash
# 安装依赖
pip install beautifulsoup4

# 运行爬虫
python baike_spider/spider_main.py
```

## License

MIT
