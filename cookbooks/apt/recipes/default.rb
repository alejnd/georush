#
# Cookbook Name:: apt
# Recipe:: default
#
# Copyright (c) 2016 The Authors, All Rights Reserved.
execute "apt-get update" do
   command "apt-get update"
   end
