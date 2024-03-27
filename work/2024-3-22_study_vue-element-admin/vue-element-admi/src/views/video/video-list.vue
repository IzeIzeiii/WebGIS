<template>
  <div class="video-list">
    <el-container>
      <el-header class="top">
        <el-menu
          :default-active="activeIndex2"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
        >
          <el-menu-item @click="$router.push('/good/list')">首页</el-menu-item>
          <el-menu-item @click="myThrottleCkAdder">自定义节流加载</el-menu-item>
          <el-menu-item @click="lodashDebouncedCkAdder"
            >lodash防抖加载</el-menu-item
          >
          <el-menu-item @click="lodashThrottleCkAdder"
            >lodash节流加载</el-menu-item
          >
          <el-menu-item @click="reset">重置</el-menu-item>
        </el-menu>
      </el-header>
      <div class="video-container">
        <el-card class="video-card" v-for="(e, i) in tableData" :key="i">
          <div>
            <!-- <img :src="e.children[0].model.resource.cover" /> -->
            <el-image
              style="width: 100%"
              :src="e.children[0].model.resource.cover"
              fit="cover"
            />
          </div>
          <div>{{ e.children[0].model.resource.title }}</div>
          <div class="content">
            {{ e.children[0].model.resource.content }}
          </div>
        </el-card>
      </div>
    </el-container>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";

export default {
  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1",
      tableData: [],
      myDebouncedCkAdder: this.myDbcd(this.addCkData, 1000),
      myThrottleCkAdder: this.myThrt(this.addCkData, 1000),
      lodashDebouncedCkAdder: _.debounce(this.addCkData, 1000),
      lodashThrottleCkAdder: _.throttle(this.addCkData, 1000),
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    myDbcd(fn, t) {
      let tid;
      return (...args) => {
        clearTimeout(tid);
        tid = setTimeout(() => {
          fn(...args);
        }, t);
      };
    },
    myThrt(fn, t) {
      let fl = true;
      return (...args) => {
        if (fl) {
          fn(...args);
          fl = false;
          setTimeout(() => (fl = true), t);
        }
      };
    },
    addCkData() {
      axios.get("https://apis.netstart.cn/xpc/home/vmovier").then((res) => {
        this.tableData = this.tableData.concat(res.data.data.children);
        console.log(res.data.data.children);
      });
    },
    reset() {
      axios.get("https://apis.netstart.cn/xpc/home/vmovier").then((res) => {
        this.tableData = res.data.data.children;
        console.log("reset");
      });
    },
  },
  mounted: function () {
    axios.get("https://apis.netstart.cn/xpc/home/vmovier").then((res) => {
      this.tableData = res.data.data.children;
      console.log(res.data.data.children);
    });
  },
};
</script>
<style>
.el-header {
  padding: 0 !important;
}

.video-list {
  padding: 0px;
  margin: 0px;
  height: 100%;
}

/* .el-container {
  height: 100%;
} */
.video-card {
  margin: 0 0 10px 0;
  width: 200px;
}

.content {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.video-container {
  padding: 20px;
  display: flex;
  flex-direction: row;
  flex-wrap : wrap;
  justify-content:space-around;
}

.video-img{
  margin: 0;
}
</style>
