using System;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Media;

// https://go.microsoft.com/fwlink/?LinkId=402352&clcid=0x804 上介绍了“空白页”项模板

namespace App_developer
{
    /// <summary>
    /// 可用于自身或导航至 Frame 内部的空白页。
    /// </summary>
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {

        }

        private async void Button_Click_1(object sender, RoutedEventArgs e)
        {
            Button b = (Button)sender;
            b.Foreground = new SolidColorBrush(Windows.UI.Colors.Bisque);
            ContentDialog Connect_to = new ContentDialog
            {
                Title = "404 Not Found",
                Content = "抱歉，暂无历史信息！",
                CloseButtonText = "Cancel",
                DefaultButton = ContentDialogButton.Close,
            };
            ContentDialogResult result = await Connect_to.ShowAsync();
        }

        private async void Button_Click_2Async(object sender, RoutedEventArgs e)
        {
            Button b = (Button)sender;
            b.Foreground = new SolidColorBrush(Windows.UI.Colors.Bisque);
            ContentDialog Tishi = new ContentDialog
            {
                Title = "Confirm calling",
                Content = "我们将建立与被监护端的通讯，是否要继续建立通话？",
                CloseButtonText = "Cancel",
                PrimaryButtonText = "Video Calling",
                SecondaryButtonText = "Audio Calling",
                DefaultButton = ContentDialogButton.Primary,
            };
            ContentDialogResult result = await Tishi.ShowAsync();


        }


        private async void Button_Click_2(object sender, RoutedEventArgs e)
        {
            ContentDialog Info = new ContentDialog
            {
                Title = "开发者日常一皮",
                Content = "这是一个零基础开发者在大佬带飞下几天内肝出来的Demo，敬请期待",
                CloseButtonText = "好的，我会支持你的",
                PrimaryButtonText = "虽然不情愿还是支持下",
                DefaultButton = ContentDialogButton.Close,
            };
            ContentDialogResult result = await Info.ShowAsync();
        }
        private void HyperlinkButton_Click(object sender, RoutedEventArgs e)
        {
            this.Frame.Navigate(typeof(HistoryPage));
        }

    }
}
