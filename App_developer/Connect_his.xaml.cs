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

// https://go.microsoft.com/fwlink/?LinkId=234238 上介绍了“空白页”项模板

namespace App_developer
{
    /// <summary>
    /// 可用于自身或导航至 Frame 内部的空白页。
    /// </summary>
    public sealed partial class Connect_his : Page
    {   
        public Connect_his()
        {
            this.InitializeComponent();
            this.ViewModel = new RecordingViewModel_1();
        }
        public RecordingViewModel_1 ViewModel { get; set; }




        private void Button_Click(object sender, RoutedEventArgs e)
        {
            this.Frame.Navigate(typeof(MainPage));
        }

    }

    public class RecordingViewModel_1
    {
        private Recording_1 defaultRecording_1 = new Recording_1();
        public Recording_1 DefaultRecording_1 { get { return this.defaultRecording_1; } }

    }

    public class Recording_1
    {
        public string Towhom { get; set; }
        public string StartTime { get; set; }
        public int Time_Last { get; set; }
        public Recording_1()
        {
            this.Towhom = "经纪人";
            this.StartTime = "2019/06/22 19:51";
            this.Time_Last = 1200;
        }
        public string OneLineSummary_1
        {
            get
            {
                return $"{this.Towhom}            {this.StartTime}                     "
                    + this.Time_Last + "秒";
            }
        }

    }

}
