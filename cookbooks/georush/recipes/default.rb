#
# Cookbook Name:: georush
# Recipe:: default
#
# Copyright (c) 2016 The Authors, All Rights Reserved.
include_recipe "apt"

package 'python3' do
  action :install
end

package 'geoip-bin' do
  action :install
end

package 'geoip-database' do
  action :install
end

cookbook_file "/root/georush.py" do
  source "georush.py"
  mode "0774"
end
