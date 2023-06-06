<template>
	<view class="content">
    <view class="home-box">
      <view class="home-nav">
        <view class="_h1">员工信息采集系统V1.0</view>
        <view class="nav-header">
          <u-grid
            :border="false"
            col="3"
          >
            <u-grid-item
              v-for="(listItem,listIndex) in list"
              :key="listIndex"
            >
                <u-icon
                  :customStyle="{paddingTop:20+'rpx'}"
                  :name="listItem.name"
                  :size="22"
                ></u-icon>
                <text class="grid-text">{{listItem.title}}</text>
            </u-grid-item>
          </u-grid>
          <u-toast ref="uToast" />
        </view>

      </view>
      <view class="nav-main">
        <u-grid
              :border="false"
              col="4"
      >
          <u-grid-item
                  v-for="(listItem,listIndex) in list2"
                  :key="listIndex"
          >
              <u-icon
                      :customStyle="{paddingTop:20+'rpx'}"
                      :name="listItem.name"
                      :size="22"
              ></u-icon>
              <text class="grid-text">{{listItem.title}}</text>
          </u-grid-item>
      </u-grid>
      <u-toast ref="uToast" />
      </view>
    </view>
    <view class="u-page">
      <u-list
          @scrolltolower="scrolltolower"
        >
          <u-list-item
            v-for="(item, index) in indexList"
            :key="index"
          >
            <u-cell
              :title="`列表长度-${index + 1}`"
            >
              <u-avatar
                slot="icon"
                shape="square"
                size="35"
                :src="item.url"
                customStyle="margin: -3px 5px -3px 0"
              ></u-avatar>
            </u-cell>
          </u-list-item>
        </u-list>
    </view>

    <u-tabbar
    	:value="value6"
    	@change="name => value6 = name"
    	:fixed="true"
    	:placeholder="true"
    	:safeAreaInsetBottom="true"
    >
    	<u-tabbar-item text="首页" icon="home" ></u-tabbar-item>
    	<u-tabbar-item text="我的" icon="account" ></u-tabbar-item>
    </u-tabbar>
	</view>
</template>

<script>
	export default {
		data() {
			return {
        list: [{
            name: 'photo',
            title: '图片'
          },
          {
            name: 'lock',
            title: '锁头'
          },
          {
            name: 'star',
            title: '星星'
          }
        ],
      list2: [{
            name: 'photo',
            title: '图片'
            },
            {
                name: 'lock',
                title: '锁头'
            },
            {
                name: 'star',
                title: '星星'
            },
            {
                name: 'hourglass',
                title: '沙漏'
            },
            {
                name: 'home',
                title: '首页'
            },
            {
                name: 'star',
                title: '音量'
            },
            {
                name: 'home',
                title: '首页'
            },
            {
                name: 'star',
                title: '音量'
            }
        ],
        value6: 0,
        indexList: [],
          urls: [
            'https://cdn.uviewui.com/uview/album/1.jpg',
            'https://cdn.uviewui.com/uview/album/2.jpg',
            'https://cdn.uviewui.com/uview/album/3.jpg',
            'https://cdn.uviewui.com/uview/album/4.jpg',
            'https://cdn.uviewui.com/uview/album/5.jpg',
            'https://cdn.uviewui.com/uview/album/6.jpg',
            'https://cdn.uviewui.com/uview/album/7.jpg',
            'https://cdn.uviewui.com/uview/album/8.jpg',
            'https://cdn.uviewui.com/uview/album/9.jpg',
            'https://cdn.uviewui.com/uview/album/10.jpg',
          ]
			}
		},
		onLoad() {
      this.loadmore()
		},
		methods: {
      click(name) {
        this.$refs.uToast.success(`点击了第${name}个`)
      },
      scrolltolower() {
        this.loadmore()
      },
      loadmore() {
        for (let i = 0; i < 30; i++) {
          this.indexList.push({
            url: this.urls[uni.$u.random(0, this.urls.length - 1)]
          })
        }
      }
		}
	}
</script>

<style lang="scss">
  @import "@/uni_modules/uview-ui/index.scss";
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
    .u-page {
    	width: 100%;
    }
    .home-box {
      width: 100%;
      background-color: #999999;
      .home-nav {
        // display: flex;
        background: url('../../static/bg.jpg') no-repeat center top;
        background-size: 100%;
        position: relative;
        margin-bottom: 30px;
        ._h1 {
          color: #ffffff;
          min-height: 180px;
        }
        .nav-header {
          background-color: #ffffff;
          width: 94%;
          margin: 0 auto;
          padding-bottom: 15px;
          border-radius: 10px;
          bottom: -30px;
          left: 3%;
          position: absolute;
        }
      }
      .nav-main {
        background-color: #ffffff;
        width: 94%;
        margin: 40px auto 10px;
        border-radius: 10px;
        padding-bottom: 10px;
      }
    }
	}

</style>
