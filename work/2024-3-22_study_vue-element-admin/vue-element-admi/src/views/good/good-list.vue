<template>
  <div class="good-list">
    <!-- 筛选面板 -->
    <el-row>
      <el-col :span="24">
        <el-input style="width: 135px" placeholder="请输入内容"></el-input>
        <el-select v-model="value" placeholder="请选择">
          <el-option
            v-for="item in cates"
            :key="item.id"
            :label="item.cate_zh"
            :value="item.cate"
          >
          </el-option>
        </el-select>
        <el-date-picker
          type="daterange"
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
        >
        </el-date-picker>
        <el-button type="primary" icon="el-icon-search">搜索</el-button>
        <el-button type="primary" icon="el-icon-edit" @click="$router.push('/good/add')">添加</el-button>
        <el-button type="primary" icon="el-icon-download">导出</el-button>
        <el-checkbox style="margin-left: 20px">审核人</el-checkbox>
      </el-col>
    </el-row>

    <!-- 表格 -->
    <el-table :data="list" border style="width: 100%; margin-top: 20px">
      <el-table-column
        prop="id"
        label="序号"
        align="center"
        sortable
        width="180"
      >
        <template slot-scope="{ $index }">
          <div>{{ $index + 1 }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="name" label="商品" align="center" width="180">
        <template slot-scope="{ row }">
          <img :src="row.img" style="width: 60px" alt="" />
          <div>{{ row.name }}</div>
        </template>
      </el-table-column>

      <el-table-column prop="price" label="价格" align="center">
        <template slot-scope="{ row }">
          <div>{{ `￥${row.price.toFixed(2)}` }}</div>
        </template>
      </el-table-column>

      <el-table-column prop="cate" label="品类" align="center">
        <template slot-scope="{ row }">
          <div>{{ row.cate }}</div>
        </template>
      </el-table-column>

      <el-table-column prop="hot" label="是否热销" align="center">
        <template slot-scope="{ row }">
          <div>{{ row.hot ? "是" : "否" }}</div>
        </template>
      </el-table-column>

      <el-table-column prop="create_time" label="发布时间" align="center">
        <template slot-scope="{ row }">
          <div>{{ row.create_time }}</div>
        </template>
      </el-table-column>

      <el-table-column prop="check_status" label="商品状态" align="center">
        <template slot-scope="{ row }">
          <div>{{ row.check_status ? "已上架" : "待审核" }}</div>
        </template>
      </el-table-column>

      <el-table-column label="操作" width="230" align="center">
        <template slot-scope="{ row }">
          <el-button type="primary" size="mini">编辑</el-button>
          <el-button v-if="row.published" type="primary" size="mini"
            >详情</el-button
          >
          <el-button v-else type="success" size="mini">审核</el-button>
          <el-button size="mini" type="danger">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 分页 -->
    <el-pagination
      style="margin-top: 20px"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="page"
      :page-sizes="[2, 5, 10, 20]"
      :page-size="size"
      layout="total, sizes, prev, pager, next, jumper"
      :total="400"
    >
    </el-pagination>
  </div>
</template>

<script>
export default {
  name: "good",
  props: [],
  data() {
    return {
      cates: [
        { id: 1, cate_zh: "电器", cate: "dianqi" },
        { id: 2, cate_zh: "生活", cate: "shenghuo" },
      ],
      list: [
        {
          id: 1,
          create_time: "2016-05-02",
          name: "小米手机",
          address: "上海市普陀区金沙江路 1518 弄",
          img: "https://img10.360buyimg.com/mobilecms/s360x360_jfs/t1/132363/40/2790/109217/5ef04734E44252d8a/c9f28f327259059e.jpg!q70.dpg.webp",
          price: 199,
          cate: "phone",
          hot: true,
          published: false,
          check_status: false,
        },
        {
          id: 2,
          create_time: "2016-05-02",
          name: "小米手机",
          address: "上海市普陀区金沙江路 1518 弄",
          img: "https://img10.360buyimg.com/mobilecms/s360x360_jfs/t1/132363/40/2790/109217/5ef04734E44252d8a/c9f28f327259059e.jpg!q70.dpg.webp",
          price: 199,
          cate: "phone",
          hot: false,
          published: true,
          check_status: true,
        },
      ],
      page: 1,
      size: 2,
    };
  },
  methods: {
    // 改变一页显示多少条数据触发
    handleSizeChange() {},
    // 点击页码触发
    handleCurrentChange() {},
  },
};
</script>

<style scoped>
.good-list {
  padding: 20px;
  box-sizing: border-box;
}
</style>