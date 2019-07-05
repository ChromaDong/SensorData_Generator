using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

// https://go.microsoft.com/fwlink/?LinkId=402352&clcid=0x804 上介绍了“空白页”项模板

namespace LemonGit
{
    /// <summary>
    /// 可用于自身或导航至 Frame 内部的空白页。
    /// </summary>
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
            this.ViewModel = new loginViewModel();
        }
        public loginViewModel ViewModel { get; set; }
        private void TextBlock_SelectionChanged(object sender, RoutedEventArgs e)
        {

        }

        private void TryButton_Click(object sender, RoutedEventArgs e)
        {

        }
    }

    public class LoginClass
    {
        public Boolean isLogin { get; set; }
        public DateTime loginTime { get; set; }
        public LoginClass()
        {
            this.isLogin = false;
            this.loginTime = new DateTime(2006, 7, 5);
        }


        public string tellLoginSituation
        {
            get
            {
                
                if(this.isLogin==true)
                {
                    return $"You have login! at:" + this.loginTime.ToString("d");
                }
                else
                {
                    return $"You have \n not login. \n Last login at: \n " + this.loginTime.ToString("d");
                }
            }
        }

        

    }
    public class loginViewModel
    {
        private LoginClass userlogin = new LoginClass();
        public  LoginClass UserLogin
        {
            get
            {
                return this.userlogin;
            }
        }
    }

}
