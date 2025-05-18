
import React from 'react';
import { Layout, Menu, Button, Dropdown, Space, } from 'antd';
import './home.css'
import { ProjectOutlined, DatabaseOutlined, DashboardOutlined, CloudServerOutlined, CodeOutlined, DownloadOutlined, SunOutlined, MoonOutlined, CloudUploadOutlined, DownOutlined } from '@ant-design/icons';
const { Header, Footer, Sider, Content } = Layout;
import { useNavigate, Outlet, useLocation } from "react-router-dom";

export default function Home () {

    const navigate = useNavigate();
    const location = useLocation();
    const systemMsg = [
    {
        key: '1',
        label: '消息1',
    },
    {
        key: '2',
        label: '消息2',
    }
    ];

    const menuProps = {
        items: systemMsg
    }

    const items = [
        {
            key: 'sub1',
            label: '数据看板',
            icon: <DashboardOutlined />,
        },
        {
            key: 'sub2',
            label: '项目管理',
            icon: <ProjectOutlined />,
        },
        {
            key: 'sub3',
            label: '数据库管理',
            icon: <DatabaseOutlined />,
        },
        {
            key: 'sub4',
            label: '任务管理',
            icon: <CodeOutlined />,
        },
        {
            type: 'divider',
        },
        {
            key: 'sub5',
            label: '服务器管理',
            icon: <CloudServerOutlined />,
        }

    ];

    const handleClick = (e) => {
        const routeMap = {
            sub1: 'Whiteboard',
            sub2: 'Projectboard',
            sub3: 'Sqlboard',
            sub4: 'SqlTable',
            sub5: 'SurfManager',
        };
        navigate(`/${routeMap[e.key]}`);
    };

    const pathToKey = {
        '/Whiteboard': 'sub1',
        '/Projectboard': 'sub2',
        '/Sqlboard': 'sub3',
        '/SqlTable': 'sub4',
        '/SurfManager': 'sub5',
    };

    return (
        <>
           <Layout className='page-layout'>
                <Header className='page-header'>
                    <div>
                        <img src="" alt="" />
                        <span className='title'>
                            Plum
                        </span>
                    </div>
                    <div className='btn-group'>

                        <Dropdown menu={{ items: systemMsg }}>
                            <a onClick={e => e.preventDefault()}>
                                <Space>
                                    系统通知
                                    <DownOutlined />
                                </Space>
                            </a>
                        </Dropdown>

                        
                        <Button type="primary" icon={<MoonOutlined />} className='darkmode'>
                            深色模式
                        </Button>
                        <Button type="primary" icon={<CloudUploadOutlined />} className='darkmode'>
                            版本信息：1.0
                        </Button>
                    </div>
                </Header>
                
                <Layout className='page-content'>

                    <Sider className='page-content-sider'>
                        <Menu
                            onClick={handleClick}
                            style={{ width: "100%", paddingTop: "1rem" }}
                            selectedKeys={[pathToKey[location.pathname]]}
                            defaultSelectedKeys={["sub1"]}
                            defaultOpenKeys={['sub1']}
                            mode="inline"
                            items={items}
                        />
                    </Sider>

                    <Content>
                        <Outlet/>
                    </Content>

                </Layout>
            </Layout> 
        </>
    )
}