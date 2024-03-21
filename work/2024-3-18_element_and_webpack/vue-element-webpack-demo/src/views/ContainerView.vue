<template>
  <div class="index">
    <el-container>
      <el-header class="top">
        <el-menu :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" @select="handleSelect"
          background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
          <el-menu-item @click="myDebouncedCkAdder">自定义防抖加载</el-menu-item>
          <el-menu-item @click="myThrottleCkAdder">自定义节流加载</el-menu-item>
          <el-menu-item @click="lodashDebouncedCkAdder">lodash防抖加载</el-menu-item>
          <el-menu-item @click="lodashThrottleCkAdder">lodash节流加载</el-menu-item>
          <el-menu-item @click="reset">重置</el-menu-item>
        </el-menu>
      </el-header>
      <el-container>
        <el-aside>
          <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose"
            background-color="#548584" text-color="#fff" active-text-color="#ff804b">
            <el-submenu index="1">
              <template slot="title">
                <i class="el-icon-location"></i>
                <span>导航一</span>
              </template>
              <el-menu-item-group>
                <template slot="title">分组一</template>
                <el-menu-item index="1-1">选项1</el-menu-item>
                <el-menu-item index="1-2">选项2</el-menu-item>
              </el-menu-item-group>
              <el-menu-item-group title="分组2">
                <el-menu-item index="1-3">选项3</el-menu-item>
              </el-menu-item-group>
              <el-submenu index="1-4">
                <template slot="title">选项4</template>
                <el-menu-item index="1-4-1">选项1</el-menu-item>
              </el-submenu>
            </el-submenu>
            <el-menu-item index="2">
              <i class="el-icon-menu"></i>
              <span slot="title">导航二</span>
            </el-menu-item>
            <el-menu-item index="3" disabled>
              <i class="el-icon-document"></i>
              <span slot="title">导航三</span>
            </el-menu-item>
            <el-menu-item index="4">
              <i class="el-icon-setting"></i>
              <span slot="title">导航四</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <el-table :data="tableData" height="100%" stripe >
            <el-table-column prop="children[0].model.resource.cover" label="图片" width="180">
              <template slot-scope="scope">
                <el-image style="width: 160px; height: 90px" :src="scope.row.children[0].model.resource.cover" fit="cover"></el-image>
              </template>
            </el-table-column>
            <el-table-column prop="children[0].model.resource.title" label="标题" width="180">
            </el-table-column>
            <el-table-column prop="children[0].model.resource.content" label="描述">
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
const axios = require("axios");
import _ from "lodash";

export default {
  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1",
      tableData: [],
      myDebouncedCkAdder:this.myDbcd(this.addCkData,1000),
      myThrottleCkAdder:this.myThrt(this.addCkData,1000),
      lodashDebouncedCkAdder:_.debounce(this.addCkData,1000),
      lodashThrottleCkAdder:_.throttle(this.addCkData,1000)
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
    myDbcd(fn,t){
      let tid;
      return (...args)=>{
        clearTimeout(tid);
        tid=setTimeout(()=>{
          fn(...args);
        },t);
      };
    },
    myThrt(fn,t){
      let fl=true;
      return (...args)=>{
        if(fl) {
          fn(...args);
          fl=false;
          setTimeout(()=>fl=true,t);
        };
      }
    },
    addCkData(){
      axios.get("https://apis.netstart.cn/xpc/home/vmovier").then((res) => {
        this.tableData=this.tableData.concat(res.data.data.children);
        console.log(res.data.data.children);
      });
    },
    reset(){
      axios.get("https://apis.netstart.cn/xpc/home/vmovier").then((res) => {
        this.tableData=(res.data.data.children);
        console.log('reset');
      });
    }
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
/* .el-header,
.el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body>.el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
} */
.el-header {
  padding: 0 !important;
}

.el-aside {
  background-color: #548584;
  width: 250px !important;
}

.index {
  padding: 0px;
  margin: 0px;
  height: 100%;
}

.el-container {
  height: 100%;
}
</style>
